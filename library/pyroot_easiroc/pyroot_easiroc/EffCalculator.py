import enum
import numpy as np
from tqdm import tqdm
from .TrackSeeker import TrackSeeker
import ROOT as r
r.gROOT.SetBatch()


class EffCalculator(TrackSeeker):
    def __init__(self, n_hit, tree_name, filepath):
        super().__init__(tree_name, filepath)
        self._n_hit_required = n_hit
        self._exec_landau_fit()
        self._search_all_vertical_mu_event()

    def _prepare_variables(self):
        super()._prepare_variables()
        self._vertical_event_list = [[] for _ in range(len(self.VERTICAL_GROUP))]

    def _exec_landau_fit(self):
        self._fitted_MPV_s = np.zeros(64, dtype=np.float)
        for ch in range(64):
            self.fit_by_landau(ch)
            self._fitted_MPV_s[ch] = self._f_landau[ch].GetParameter(1)

    def _search_vertical_mu_event(self, vertical_group_index, VadcHigh, i_event):
        target_vertical_channels = np.array(self.VERTICAL_GROUP[vertical_group_index])
        n_vertical_hit = np.sum(self._fitted_MPV_s[target_vertical_channels] < VadcHigh[target_vertical_channels])
        if n_vertical_hit > self._n_hit_required:
            self._vertical_event_list[vertical_group_index].append(i_event)

    def _search_all_vertical_mu_event(self):
        for i_event in tqdm(range(self._n_event), desc="search vertical"):
            self.GetEntry(i_event)
            VadcHigh_np = np.array(self.VadcHigh)
            for vertical_group_index in range(len(self.VERTICAL_GROUP)):
                self._search_vertical_mu_event(vertical_group_index, VadcHigh_np, i_event)
        self._vertical_event_list_sum = set()
        for vertical_events in self._vertical_event_list:
            for vertical_event in vertical_events:
                self._vertical_event_list_sum.add(vertical_event)
        self._vertical_event_list_sum = sorted(list(self._vertical_event_list_sum))

    def _set_threshold(self, ch, adc_th):
        super().set_threshold(ch, adc_th)

    def determine_hits(self, adc_threshold_s: list):
        self._is_hit = []
        if type(adc_threshold_s) != list:
            print("invalid arg type")
        if len(adc_threshold_s) != 64:
            print("invalid arg list length")
        for ch in range(64):
            self._set_threshold(ch, adc_threshold_s[ch])
        self.determine_hit_by_landau_fit()

    def calc_effeciency(self, ch_target):
        print("this method is unused")
        exit()

    def _calc_effeciency(self, ch_target):
        for i, group in enumerate(self.VERTICAL_GROUP):
            if ch_target in group:
                vertical_group_index = i
        n_hitted = 0
        for i_event in self._vertical_event_list[vertical_group_index]:
            if self._is_hit[i_event][ch_target]:
                n_hitted += 1
        if len(self._vertical_event_list[vertical_group_index]) == 0:
            return -1
        eff = n_hitted / len(self._vertical_event_list[vertical_group_index])
        return eff

    def get_64ch_effeciency(self):
        ret = []
        for ch in tqdm(range(64), desc="calc eff"):
            ret.append(self._calc_effeciency(ch))
        return ret

    def determine_hit_by_landau_fit(self):
        self._is_hit = np.zeros([self._n_event, 64], dtype=np.int)
        is_hit = np.zeros(64, dtype=np.bool)
        self._threshold = np.array(self._threshold)
        for i_event in tqdm(self._vertical_event_list_sum):
            self.GetEntry(i_event)
            VadcHigh = np.array(self.VadcHigh)
            is_hit = self._threshold < VadcHigh
            self._is_hit[i_event] = np.array(is_hit, dtype=np.bool)
