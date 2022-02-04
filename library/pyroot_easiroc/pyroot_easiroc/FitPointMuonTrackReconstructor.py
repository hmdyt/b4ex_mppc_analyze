import os
from .TrackReconstructorBase import TrackReconstructorBase
import numpy as np
from tqdm import tqdm
import itertools

class FitPointMuonTrackReconstructor(TrackReconstructorBase):
    def __init__(self, rootfile_path, threshold_s) -> None:
        super().__init__(rootfile_path, threshold_s)
        self._hit_array = self._hit_array_gen.get_hit_array()
    
    def _pre_cut(self):
        fight = "眠い、明日書く"