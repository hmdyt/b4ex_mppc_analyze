from . import calibrationUtils
import ROOT as r
from copy import copy
from tqdm import tqdm
import os

class ExtendedTTree(r.TChain):
    _root_file_name = ""
    _hists_VadcHigh = ["unko" for _ in range(64)]
    _funcs_pedestal_fit = ["unko" for _ in range(64)]
    _n_events = None

    def __init__(self, tree_name, tree_title, root_file_name):
        super().__init__(tree_name, tree_title)
        self._root_file_name = root_file_name
        self.Add(self._root_file_name)
        self._n_events = self.GetEntries()

        for i in tqdm(range(64), desc="[tree->hist]"):
            self.construct_hist_VadcHigh(i)

    def construct_hist_VadcHigh(self, ch):
        hist = r.TH1D(
            "VadcHigh {}ch".format(ch),
            "VadcHigh {}ch;ADC;events".format(ch),
            4096, 0, 4096
        )
        # FOR DEBUG
        for i in range(1000):
        #for i in tqdm(range(self._n_events)):
            self.GetEntry(i)
            hist.Fill(self.VadcHigh[ch])

        self._hists_VadcHigh[ch] = hist

    def fit_pedestal(self, ch, xmin, xmax):
        func = r.TF1("func ch{}".format(ch), "gaus", xmin, xmax)
        self._hists_VadcHigh[ch].Fit(func, "R")
        self._funcs_pedestal_fit[ch] = func

    def fit_pedestal_auto_range(self, ch):
        xmin = 0
        xmax = 4096
        while self._hists_VadcHigh[ch].GetBinContent(xmin) == 0: xmin += 1
        while self._hists_VadcHigh[ch].GetBinContent(xmax) == 0: xmax -= 1
        self._hists_VadcHigh[ch].GetXaxis().SetRangeUser(xmin, xmax)
        self.fit_pedestal(ch, xmin, xmax)

    def get_pedestal_fit_params(self, ch):
        func = self._funcs_pedestal_fit[ch]
        ret = {
            "constant": (func.GetParameter(0), func.GetParError(0)),
            "mean": (func.GetParameter(1), func.GetParError(1)),
            "sigma": (func.GetParameter(2), func.GetParError(2))
        }
        return ret

    def save_hist_VadcHigh(self, ch, save_dir_path="./"):
        dir_name = "img_" + self._root_file_name.split('/')[-1].replace(".root", "").replace("root", "") + '/'
        os.mkdir(save_dir_path + dir_name)
        hist = self._hists_VadcHigh[ch]
        canvas = r.TCanvas()
        hist.Draw()
        canvas.SaveAs(save_dir_path + dir_name + "VadcHigh_{}ch.png".format(ch))

    def save_hists_VadcHigh(self, save_dir_path="./"):
        for ch in tqdm(range(64), desc="[img saving]"):
            self.save_hist_VadcHigh(ch, save_dir_path)