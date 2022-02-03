from re import S
from .TrackReconstructorBase import TrackReconstructorBase
import numpy as np
from tqdm import tqdm
import itertools


class MuonTrackReconstructor(TrackReconstructorBase):
    def __init__(self, rootfile_path, threshold_s) -> None:
        super().__init__(rootfile_path, threshold_s)
        self._hit_array = self._hit_array_gen.get_hit_array()
        print(self._hit_array.shape[0])
    
    def _pre_cut_threshold_layer(self):
        self._layer_n_hit = np.sum(self._hit_array, axis = (2,3))
        self._hit_layer_number = np.count_nonzero(self._layer_n_hit, axis=1)
        self._threshold_layer_number = 8
        self._pre_cut_index = np.where(self._hit_layer_number >= self._threshold_layer_number)[0]
        self._pre_cut_array = self._hit_array[self._pre_cut_index]
        print("preselected, {:.2f}% remain".format(
            100 * self._pre_cut_array.shape[0] / self._hit_array.shape[0]
        ))

    def hit_muon_straight(self):
        self._hit_muon_index = []
        
        for i_event in tqdm(self._pre_cut_array):
            for i_layer, i,j in itertools.product(range(8), range(4), range(4)):
                if(i_layer == 7): 
                    self._hit_muon_index.append(i_event)
                    break
                    
                if (i_event[i_layer][i][j] == 1):
                    if(i == 0):
                        hit_slice = i_event[i_layer + 1:i_layer + 3, 0:i+2, j-1:j+2]
                        if(np.all(hit_slice == 0)):
                            break
                        continue
                    
                    if(j == 0):
                        hit_slice = i_event[i_layer + 1:i_layer + 3,i-1:i+2, 0:j+2]
                        if(np.all(hit_slice == 0)):
                            break
                        continue
                    
                    else:
                        hit_slice = i_event[i_layer + 1:i_layer + 3,i-1:i+2, j-1:j+2]
                        if(np.all(hit_slice == 0)):
                            break
                        continue

        print(len("straight event is ",self._hit_muon_index))
        print("selected straight event, {:.2f}% remain".format(
            100 * len(self._hit_muon_index) / self._pre_cut_array.shape[0]
        ))                     