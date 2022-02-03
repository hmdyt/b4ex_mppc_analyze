from typing import List
import numpy as np
import networkx as nx
from .TrackReconstructorBase import TrackReconstructorBase


class PionTrackReconstructor(TrackReconstructorBase):
    def __init__(self, rootfile_path: str, threshold_s: List[int]) -> None:
        super().__init__(rootfile_path, threshold_s)
        self._preselect()

    def _preselect(self):
        """
        1番上のlayerで1つだけ鳴ったイベントを集める
        """
        self._layer_n_hits = np.sum(self._hit_array, axis=(2, 3))
        layer_ref = np.array([0, 0, 0, 0, 0, 0, 0, 1])
        self._preselected_events_index = np.where(layer_ref[-1] == self._layer_n_hits.T[-1])[0]
        self._preselected_events_array = self._hit_array[self._preselected_events_index]
        print("preselected, {:.2f}% remain".format(
            100 * self._preselected_events_array.shape[0] / self._hit_array.shape[0]
        ))

    def write_preselected_event(self, i):
        self.show(self._preselected_events_index[i])

    def print_preselected_event(self, i):
        print(self._hit_array[self._preselected_events_index[i]])
