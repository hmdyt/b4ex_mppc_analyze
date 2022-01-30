from tqdm import tqdm
import ROOT as r
import numpy as np
from . import calibrationUtils as util


class TrackSeeker(r.TChain):
    OUTER_CHNNELS = set([
        0, 1, 2, 3, 60, 61, 62, 63,
        28, 29, 30, 31, 32, 33, 34, 35
        ])
    INNER_CHANNELS = set(range(64)) - OUTER_CHNNELS
    VERTICAL_GROUP_EAST_BOARD = tuple(
        tuple(j + 4*i for i in range(8))
        for j in range(4)
    )
    VERTICAL_GROUP_WEST_BOARD = tuple(
        tuple(reversed([32 + j + 4*i for i in range(8)]))
        for j in range(4)
    )
    VERTICAL_GROUP = VERTICAL_GROUP_EAST_BOARD + VERTICAL_GROUP_WEST_BOARD

    def __init__(self, name, filepath):
        # recieve args
        super().__init__(name)
        self._filepath = filepath
        # TChain settings
        self.SetBranchStatus("*", 0)
        self.SetBranchStatus("VadcHigh")
        self.Add(self._filepath)
        # prepare member variables
        self._prepare_variables()
        # exec member functions
        self.fetch_hist()

    def _prepare_variables(self):
        self._n_event = self.GetEntries()
        self._threshold = [0 for _ in range(64)]
        self._landau_fit_range = [[1200, 2700] for _ in range(64)]
        self._f_landau = [r.TF1("f_landau{}".format(ch), "landau", 0, 4096) for ch in range(64)]
        self._is_hit = []
        self._effeciency = [None for _ in range(64)]

    def set_threshold(self, ch, adc_th):
        self._threshold[ch] = adc_th

    def fetch_hist(self):
        self._hist = [None for _ in range(64)]
        for ch in range(64):
            self._hist[ch] = util.getHistMPPC(self._filepath, ch)
        print("loaded VadcHigh 64ch as histogram")

    def set_landau_fit_range(self, ch, fit_range_min, fit_range_max):
        self._landau_fit_range[ch] = [fit_range_min, fit_range_max]

    def fit_by_landau(self, ch):
        fitmin, fitmax = self._landau_fit_range[ch]
        self._hist[ch].Fit(self._f_landau[ch], "", "", fitmin, fitmax)

    def save_hist(self):
        canvas = r.TCanvas("c", "c", 1920*2, 1080*16)
        canvas.Divide(4, 16)
        for ch in range(64):
            canvas.cd(ch+1),
            self._hist[ch].Draw()
        save_name = self._filepath.split('/')[-1].replace(".root", ".png")
        canvas.SaveAs(save_name)

    def determine_hit_by_landau_fit(self):
        tree = r.TTree("tree_bool", "tree_bool")
        is_hit = np.zeros(64, dtype=bool)
        tree.Branch("is_hit", is_hit, "is_hit[64]/O")

        self._threshold = np.array(self._threshold)
        for i_event in tqdm(range(self._n_event), desc="making is_hit", leave=False):
            self.GetEntry(i_event)
            VadcHigh = np.array(self.VadcHigh)
            is_hit = self._threshold < VadcHigh
            self._is_hit.append(is_hit)
            tree.Fill()
        # TODO: consider hit info saving
        tree.SaveAs("tmp.root")

    def calc_effeciency(self, ch_target):
        """
        this method is only used inner channel
        """
        if ch_target not in self.INNER_CHANNELS:
            print("ch {} is not inner scintillator!".format(ch_target))
            exit()
        # search upside, downside channel
        for i, group in enumerate(self.VERTICAL_GROUP):
            if ch_target in group:
                vertical_group_index = i
        for i, ch_candi in enumerate(self.VERTICAL_GROUP[vertical_group_index]):
            if ch_target == ch_candi:
                ch_down = self.VERTICAL_GROUP[vertical_group_index][i-1]
                ch_up = self.VERTICAL_GROUP[vertical_group_index][i+1]
        print("target channel of effeciency calculation is {}, up{}, down{}".format(ch_target, ch_up, ch_down))
        # calc effeciency
        ok = 0
        ng = 0
        for i_event in tqdm(range(self._n_event), desc="calc eff ch{}".format(ch_target), leave=False):
            if self._is_hit[i_event][ch_up] and self._is_hit[i_event][ch_down]:
                if self._is_hit[i_event][ch_target]:
                    ok += 1
                else:
                    ng += 1
            else:
                continue
        if (ok+ng) == 0:
            print("There is no event to calc effeciency ch {}".format(ch_target))
        else:
            self._effeciency[ch_target] = ok / (ok + ng)
            print("detectation effeciency of ch {} is {:.5f}%".format(
                ch_target,
                100*self._effeciency[ch_target]
            ))
            print("used {} events".format(ok+ng))
            