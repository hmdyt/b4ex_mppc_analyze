from .TrackReconstructorBase import TrackReconstructorBase
import numpy as np

class MuonTrackReconstructor(TrackReconstructorBase):
    def __init__(self,rootfile_path) -> None:
        super().__init__(rootfile_path)
        self._hit_array = self._hit_array_gen.get_hit_array()
    
    def hit_muon_straight(self):
        self.hit_muon = np.empty((0,8,4,4),int)
        for k in range(8):
            #k層めにイベントがなければこのイベントは無視
            if (self._hit_array[k].any() == 0):
                break
            #最後の層を見てイベントがあれば真っ直ぐミューオンが通ったイベントとしてhit_muonに詰める
            if(k == 7):
                if(self._hit_array[k].any == 0):
                    break
                self._hit_array = np.reshape(self._hit_array, (1,8,4,4))
                self.hit_muon = np.append(self.hit_muon, self._hit_array, axis=0)
                break
            
            for i in range(4):
                for j in range(4):
                    # 反応したものがあると入る分岐
                    if (self._hit_array[k][i][j] == 1):
                        # i,j =0のときのいい方法が思いつかなかったのでこの分岐方法
                        # 反応があったi,jの周り、[i-1,i,i+1][j-1,j,j+1]の最大9個の要素に1があるか確かめる
                        # i,j=1,0のような周りに９個ないものはしっかりカットされている
                        if(i == 0):
                            hit_slice = self._hit_array[k+1][0:i+2,  j-1:j+2]
                            # 全て0だったらループを抜ける
                            if(hit_slice.any() == 0):
                                break
                            continue
                        if(j ==0):
                            hit_slice = self._hit_array[k+1][i-1:i+2, 0:j+2]
                            if(hit_slice.any() == 0):
                                break
                            continue
                        else:
                            hit_slice = self._hit_array[k+1][i-1:i+2, j-1:j+2]
                            if(hit_slice.any() == 0):
                                break  
    
                              