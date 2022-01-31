import numpy as np
from tqdm import tqdm
from pyroot_easiroc.TrackSeeker import TrackSeeker
import ROOT as r
import sys
r.gROOT.SetBatch()


class EffeciencyCalc(TrackSeeker):
    def __init__(self, name, filepath):
        super().__init__(name, filepath)

    def _prepare_variables(self):
        super()._prepare_variables()
        self._ref_threshold = [0 for _ in range(64)]
        self._ref_is_hit = []
        self._n_event_calc_effeciency = [0 for _ in range(64)]
        self._valid_event_list = [[] for _ in range(len(self.VERTICAL_GROUP))]
        self._valid_event_hit = 5

    def set_ref_threshold(self, ch, adc_th):
        self._ref_threshold[ch] = adc_th
    
    def require_n_hit(self, n):
        self._valid_event_hit = n

    def fit_by_landau(self, ch):
        super().fit_by_landau(ch)
        for ch in range(64):
            self.set_ref_threshold(ch, self._f_landau[ch].GetParameter(1))
    
    def make_valid_event_list(self):
        for ch in range(64):
            self.fit_by_landau(ch)
        self._ref_threshold = np.array(self._ref_threshold)
        for i_event in tqdm(range(self._n_event), desc="valid event"):
            self.GetEntry(i_event)
            VadcHigh = np.array(self.VadcHigh)
            for vertical_group_index, vertical_chs in enumerate(self.VERTICAL_GROUP):
                n_vertical_hitted = np.sum(self._ref_threshold[np.array(vertical_chs)] < VadcHigh[np.array(vertical_chs)])
                if n_vertical_hitted > self._valid_event_list:
                    self._valid_event_list[vertical_group_index].append(i_event)

    def determine_is_hit(self):
        super().determine_hit_by_landau_fit()

    def determine_ref_is_hit(self):
        ref_is_hit = np.zeros(64, dtype=bool)
        self._ref_threshold = np.array(self._ref_threshold)
        for i_event in tqdm(range(self._n_event), desc="ref_is_hit", leave=False):
            self.GetEntry(i_event)
            VadcHigh = np.array(self.VadcHigh)
            ref_is_hit = self._ref_threshold < VadcHigh
            self._ref_is_hit.append(ref_is_hit)

    def calc_effeciency(self, ch_target):
        # search target vertical group
        for i, group in enumerate(self.VERTICAL_GROUP):
            if ch_target in group:
                vertical_group_index = i
        target_vertival_group = self.VERTICAL_GROUP[vertical_group_index]
        # calc effeciency
        ok = 0
        ng = 0
        for i_event in tqdm(self._valid_event_list[vertical_group_index], leave=False):
            n_vertical_hitted = 0
            for ch_other in target_vertival_group:
                if ch_target == ch_other:
                    continue
                n_vertical_hitted += self._ref_is_hit[i_event][ch_other]
            if n_vertical_hitted > 6:
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
            self._n_event_calc_effeciency[ch_target] = ok+ng

    def limit_n_event(self, n_event):
        self._n_event = n_event

def get_eff(adc, n_hit):
    ec = EffeciencyCalc("tree", "run017.root")
    ec.require_n_hit(n_hit)
    ec.determine_ref_is_hit()
    ec.make_valid_event_list()
    for ch in range(64): ec.set_threshold(ch, adc)
    ec.determine_is_hit()
    for ch in range(64): ec.calc_effeciency(ch)
    return ec._effeciency
    
if __name__ == "__main__":
    n_hit = int(sys.argv[1])
    fout = open("compare_eff_ped_{}hit.txt".format(n_hit), 'w')
    g = [r.TGraph() for _ in range(64)]

    for ch in range(64):
        g[ch].SetMarkerStyle(8)
        g[ch].SetTitle("ch{} n={};Threshold ADC Value;Effeciency".format(ch, n_hit))
    for adc in tqdm(range(900, 1500, 2), desc="ADC"):
        res = get_eff(adc, n_hit)
        for ch in range(64):
            if res[ch] == None: continue
            g[ch].SetPoint(g[ch].GetN(), adc, res[ch])
        fout.write("{} ".format(adc))
        fout.write(" ".join(map(str, res)) + "\n")
    
    canvas = r.TCanvas("c", "c", 1920*2, 1080*16)
    canvas.Divide(4, 16)
    for ch in range(64):
        canvas.cd(ch+1)
        g[ch].Draw("AP")
    canvas.SaveAs("compare_effeciency_by_pedestal.png")
