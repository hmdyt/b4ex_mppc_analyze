from re import S
import os
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
        self._threshold_layer_number = 6
        self._pre_cut_index = np.where(self._hit_layer_number >= self._threshold_layer_number)[0]
        self._pre_cut_array = self._hit_array[self._pre_cut_index]
        print("preselected, {:.2f}% remain".format(
            100 * self._pre_cut_array.shape[0] / self._hit_array.shape[0]
        ))

    # 全ての層を見て、1つの層以上で決めたヒット数よりも多いものを選び出す
    def _multi_hit(self):
        self._multi_hit_event_index = []
        self._threshold_hit = 4
        for i_event in tqdm(self._pre_cut_index):
            if (np.any(self._layer_n_hit[i_event] >= self._threshold_hit)):
                self._multi_hit_event_index.append(i_event)

        print("multi_hit event is ",len(self._multi_hit_event_index))
        print("selected multi_hit event, {:.2f}% remain".format(
            100 * len(self._multi_hit_event_index) / self._hit_array.shape[0]
        )) 

    # 決めた層よりも下の層でいくつ鳴ったかでふるいに掛ける
    def _under_layer_limit(self):
        self._under_layer_limit_index = []
        self._origin_layar = 6
        # hit_arrayは上から下層の情報なので8 - origin_layer
        self._orogin_layer_under = 8 - self._origin_layar
        for i_event in tqdm(self._multi_hit_event_index):
            if (np.any(self._layer_n_hit[i_event][0: self._orogin_layer_under] >= self._threshold_hit)):
                self._under_layer_limit_index.append(i_event)

        print("multi_hit event & under layer cut is ",len(self._under_layer_limit_index))
        print("selected multi_hit & under layer cut event, {:.2f}% remain".format(
            100 * len(self._under_layer_limit_index) / self._hit_array.shape[0]
        )) 


    def hit_muon_straight(self):
        self._hit_muon_index = []
        
        for i_event in tqdm(self._under_layer_limit_index):
            for i_layer, i,j in itertools.product(range(8), range(4), range(4)):
                if(i_layer == 7): 
                    self._hit_muon_index.append(i_event)
                    break
                    
                if (self._hit_array[i_event][i_layer][i][j] == 1):
                    if(i == 0):
                        hit_slice = self._hit_array[i_event][i_layer + 1:i_layer + 3, 0:i+2, j-1:j+2]
                        if(np.all(hit_slice == 0)):
                            break
                        continue
                    
                    if(j == 0):
                        hit_slice = self._hit_array[i_event][i_layer + 1:i_layer + 3,i-1:i+2, 0:j+2]
                        if(np.all(hit_slice == 0)):
                            break
                        continue
                    
                    else:
                        hit_slice = self._hit_array[i_event][i_layer + 1:i_layer + 3,i-1:i+2, j-1:j+2]
                        if(np.all(hit_slice == 0)):
                            break
                        continue

        print("straight event & multi_hit event & under layer cut is ",len(self._hit_muon_index))
        print("selected straight event & multi_hit event & under layer cut, {:.2f}% remain".format(
            100 * len(self._hit_muon_index) / self._hit_array.shape[0]
        ))   

    def write_fig(self, i_event):
        filename_short = self._rootfile_path.split('/')[-1]
        self._save_directory_path = "img_{}_{}_layer_hits_{}_hits_under_cut_{}_layer".format(filename_short, self._threshold_layer_number, self._threshold_hit, self._origin_layar)
        os.makedirs(self._save_directory_path, exist_ok=True)
        self._fig.write_image(self._save_directory_path + "/event{}.png".format(i_event), scale=10)
        print(self._save_directory_path + "/event{}.png".format(i_event))
        self._fig.write_html(self._save_directory_path + "/event{}.html".format(i_event))
        print(self._save_directory_path + "/event{}.html".format(i_event))