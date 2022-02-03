from re import S
from .TrackReconstructorBase import TrackReconstructorBase
import numpy as np
from tqdm import tqdm

class MuonTrackReconstructor(TrackReconstructorBase):
    def __init__(self,rootfile_path) -> None:
        super().__init__(rootfile_path)
        self._hit_array = self._hit_array_gen.get_hit_array()
        print(self._hit_array.shape[0])
    
    def _pre_cut_threshold_layer(self):
        self._layer_n_hit = np.sum(self._hit_array, axis = (2,3))
        self._hit_layer_number = np.count_nonzero(self._layer_n_hit, axis=1)
        self._threshold_layer_number = 8
        self._pre_cut_index = np.where(self._hit_layer_number >= self._threshold_layer_number)[0]
        self._pre_cut_array = self._hit_array[self._pre_cut_index]
        print(print("preselected, {:.2f}% remain".format(
            100 * self._pre_cut_array.shape[0] / self._hit_array.shape[0]
        )))

    def hit_muon_straight(self):
        self._hit_muon_index = []
        
        for i_event in tqdm(self._pre_cut_array):
            if(np.all(i_event == 0)):
                break
            for k in range(8):
                #k層めにイベントがなければこのイベントは無視
                if (np.all(i_event[k] == 0)):
                    break
                #最後の層を見てイベントがあれば真っ直ぐミューオンが通ったイベントとしてhit_muonに詰める
                if(k == 7):
                    if(np.all(i_event[k] == 0)):
                        break
                    self._hit_muon_index.append(i_event)
                    break
                
                for i in range(4):
                    for j in range(4):
                        # 反応したものがあると入る分岐
                        if (i_event[k][i][j] == 1):
                            # i,j =0のときのいい方法が思いつかなかったのでこの分岐方法
                            # 反応があったi,jの周り、[i-1,i,i+1][j-1,j,j+1]の最大9個の要素に1があるか確かめる
                            # i,j=1,0のような周りに９個ないものはしっかりカットされている
                            if(i == 0):
                                hit_slice = i_event[k+1][0:i+2,  j-1:j+2]
                                # 全て0だったらループを抜ける
                                if(np.all(hit_slice == 0)):
                                    break
                                continue
                            if(j ==0):
                                hit_slice = i_event[k+1][i-1:i+2, 0:j+2]
                                if(np.all(hit_slice == 0)):
                                    break
                                continue
                            else:
                                hit_slice = i_event[k+1][i-1:i+2, j-1:j+2]
                                if(np.all(hit_slice == 0)):
                                    break  

        print(len(self._hit_muon_index))                       