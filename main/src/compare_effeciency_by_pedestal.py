from copy import copy
import numpy as np
from tqdm import tqdm
from pyroot_easiroc.TrackSeeker import TrackSeeker
import ROOT as r
r.gROOT.SetBatch()

class EffeciencyCalc(TrackSeeker):
    def __init__(self, name, filepath):
        super().__init__(name, filepath)
    
    def _prepare_variables(self):
        super()._prepare_variables()
        self._ref_threshold = [0 for _ in range(64)]
        self._ref_is_hit = []
        self._n_event_calc_effeciency = [0 for _ in range(64)]
    
    def set_ref_threshold(self, ch, adc_th):
        self._ref_threshold[ch] = adc_th

    def fit_by_landau(self, ch):
        super().fit_by_landau(ch)
        for ch in range(64):
            self.set_ref_threshold(ch, self._f_landau[ch].GetParameter(1))
    
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
        for i_event in tqdm(range(self._n_event), leave=False):
            n_vertical_hitted = 0
            for ch_other in target_vertival_group:
                if ch_target == ch_other: continue
                n_vertical_hitted += self._ref_is_hit[i_event][ch_other]
            if n_vertical_hitted > 3:
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


def get_eff(adc_th):
    ec = EffeciencyCalc("tree", "run017.root")
    ec.limit_n_event(10000)
    for ch in range(64):
        ec.fit_by_landau(ch)
    ec.determine_ref_is_hit()
    for ch in range(64):
        ec.set_threshold(ch, adc_th)
    ec.determine_is_hit()
    for ch in range(64):
        ec.calc_effeciency(ch)
    return ec._effeciency

if __name__ == "__main__":
    graphs = [r.TGraph() for ch in range(64)]
    for adc in tqdm(range(900, 1500), leave=False, desc="adc arrange"):
        ret_eff = get_eff(adc)
        for ch in range(64):
            graphs[ch].SetPoint(graphs[ch].GetN(), adc, ret_eff[ch])

    canvas = r.TCanvas("c", "c", 1920*2, 1080*16)
    canvas.Divide(4, 16)
    for ch in range(64):
        canvas.cd(ch+1)
        graphs[ch].SetMarkerStyle(8)
        graphs[ch].SetTitle("ch{};Threshold ADC value; effeciency".format(ch))
        graphs[ch].Draw("AP")
    canvas.SaveAs("compare_effeciency_by_pedestal.png")