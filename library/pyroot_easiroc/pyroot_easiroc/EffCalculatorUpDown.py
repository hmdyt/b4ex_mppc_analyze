from typing import List
import numpy as np
import uproot


class EffCalculatorUpDown:
    CHANNELS_UPSIDE = np.array([[i for i in range(0 + (4 * layer), 4 + (4 * layer))] for layer in range(8)])
    CHANNELS_DOWNSIDE = np.fliplr(np.array([[i for i in range(60 - (4 * layer), 64 - (4 * layer))] for layer in range(8)]))
    OUTER_UP_CHNNELS = set([
        28, 29, 30, 31, 32, 33, 34, 35
    ])
    OUTER_DOWN_CHNNELS = set([
        0, 1, 2, 3, 60, 61, 62, 63
    ])
    OUTER_CHNNELS = OUTER_UP_CHNNELS | OUTER_DOWN_CHNNELS
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

    def __init__(self, tree_name, rootfile_path):
        self._load_rootfile(rootfile_path, tree_name)

    def _load_rootfile(self, rootfile_path, tree_name):
        self._rootfile_path = rootfile_path
        with uproot.open(self._rootfile_path) as file:
            self._tree = file[tree_name]
            self._VadcHigh = self._tree["VadcHigh"].array(library="np")

    def set_ref_threshold_s(self, ref_threshold_s: List[int]):
        self._ref_threshold_s = np.array(ref_threshold_s)
        self._make_ref_hit()

    def set_threshold_s(self, threshold_s: List[int]):
        self._threshold_s = np.array(threshold_s)
        self._make_is_hit()
        self._search_ref_events()

    def _make_ref_hit(self):
        self._ref_hit = self._VadcHigh > self._ref_threshold_s

    def _make_is_hit(self):
        self._is_hit = self._VadcHigh > self._threshold_s

    def _search_ref_events(self):
        self._use_index_s = dict()
        # inner channels
        for ch in self.INNER_CHANNELS:
            ch_up = self._get_upside_channel(ch)
            ch_down = self._get_downside_channel(ch)
            use_index = np.where(
                self._ref_hit.T[ch_up] * self._ref_hit.T[ch_down] == 1
            )[0]
            self._use_index_s[ch] = use_index
        # upside channels
        for ch in self.OUTER_UP_CHNNELS:
            ch_down = [None for _ in range(7)]
            ch_down[0] = self._get_downside_channel(ch)
            for i in range(1, 7):
                ch_down[i] = self._get_downside_channel(ch_down[i-1])
            ch_and = np.ones(shape=(len(self._VadcHigh)), dtype=np.bool)
            for i in range(7):
                ch_and = ch_and * self._ref_hit.T[ch_down[i]]
            use_index = np.where(
                ch_and == 1
            )[0]
            self._use_index_s[ch] = use_index
        # down side channels
        for ch in self.OUTER_DOWN_CHNNELS:
            ch_up = [None for _ in range(7)]
            ch_up[0] = self._get_upside_channel(ch)
            for i in range(1, 7):
                ch_up[i] = self._get_upside_channel(ch_up[i-1])
            ch_and = np.ones(shape=(len(self._VadcHigh)), dtype=np.bool)
            for i in range(7):
                ch_and = ch_and * self._ref_hit.T[ch_up[i]]
            use_index = np.where(
                ch_and == 1
            )[0]
            self._use_index_s[ch] = use_index

    def _calc_effeciency(self, ch) -> float:
        use_index = self._use_index_s[ch]
        ok_index = np.where(
            self._is_hit[use_index].T[ch] == 1
        )[0]
        return ok_index.shape[0] / use_index.shape[0]

    def calc_all_ch_effeciency(self):
        return list(map(self._calc_effeciency, range(64)))

    def _get_upside_channel(self, ch_target):
        for i, group in enumerate(self.VERTICAL_GROUP):
            if ch_target in group:
                vertical_group_index = i
        for i, ch_candi in enumerate(self.VERTICAL_GROUP[vertical_group_index]):
            if ch_target == ch_candi:
                ch_up = self.VERTICAL_GROUP[vertical_group_index][i+1]
        return ch_up

    def _get_downside_channel(self, ch_target):
        for i, group in enumerate(self.VERTICAL_GROUP):
            if ch_target in group:
                vertical_group_index = i
        for i, ch_candi in enumerate(self.VERTICAL_GROUP[vertical_group_index]):
            if ch_target == ch_candi:
                ch_down = self.VERTICAL_GROUP[vertical_group_index][i-1]
        return ch_down
