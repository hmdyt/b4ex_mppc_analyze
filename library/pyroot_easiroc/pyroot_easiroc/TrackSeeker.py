from tqdm import tqdm
import ROOT as r
import numpy as np
import multiprocessing
from . import calibrationUtils as util


class TrackSeeker(r.TChain):
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

    # WIP
    def determine_hit_by_landau_fit(self):
        tree = r.TTree("tree_bool", "tree_bool")
        is_hit = np.zeros(64, dtype=bool)
        tree.Branch("is_hit", is_hit, "is_hit[64]/O")

        self._threshold = np.array(self._threshold)
        for i_event in tqdm(range(self._n_event)):
            self.GetEntry(i_event)
            VadcHigh = np.array(self.VadcHigh)
            is_hit = self._threshold < VadcHigh
            tree.Fill()
        # TODO: consider hit info saving
        tree.SaveAs("tmp.root")