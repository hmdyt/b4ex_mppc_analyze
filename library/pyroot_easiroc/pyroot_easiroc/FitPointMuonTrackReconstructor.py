import os
from .TrackReconstructorBase import TrackReconstructorBase
import numpy as np
from tqdm import tqdm
import itertools
from scipy import optimize

class FitPointMuonTrackReconstructor(TrackReconstructorBase):
    def __init__(self, rootfile_path, threshold_s) -> None:
        super().__init__(rootfile_path, threshold_s)
        self._hit_array = self._hit_array_gen.get_hit_array()
    
    # 6層以上なったイベントのみを見る
    def _pre_cut_threshold_layer(self):
        self._layer_n_hit = np.sum(self._hit_array, axis = (2,3))
        self._hit_layer_number = np.count_nonzero(self._layer_n_hit, axis=1)
        self._threshold_layer_number = 6
        self._pre_cut_index = np.where(self._hit_layer_number >= self._threshold_layer_number)[0]
        print("preselected, {:.2f}% remain".format(
            100 * self._pre_cut_index.shape[0] / self._hit_array.shape[0]
        ))

    # 一番上の層で1hitのeventを保存
    def _select_top_layer_hit_event (self):
        self._select_top_layer_hit_event_index = []
        # hit_arrayは上から最下層の情報なので 8 - origin_layer
        self._threshold_hit = 1
        for i_event in tqdm(self._pre_cut_index):
            if (np.all(self._layer_n_hit[i_event][7] == self._threshold_hit)):
                self._select_top_layer_hit_event_index.append(i_event)

        print("select_top_layer_hit_event is ",len(self._select_top_layer_hit_event_index))
        print("selected select_top_layer_hit_event, {:.2f}% remain".format(
            100 * len(self._select_top_layer_hit_event_index) / self._hit_array.shape[0]
        )) 
        
    #　一番下の層で1hitのイベントを保存
    def _select_bottom_layer_hit_event (self):
        self._select_bottom_layer_hit_event_index = []
        # hit_arrayは上から最下層の情報なので 8 - origin_layer
        self._threshold_hit = 1
        for i_event in tqdm(self._select_top_layer_hit_event_index):
            if (np.all(self._layer_n_hit[i_event][0] == self._threshold_hit)):
                self._select_bottom_layer_hit_event_index.append(i_event)

        print("select_top & bottom layer_hit_event is ",len(self._select_bottom_layer_hit_event_index))
        print("selected select top & bottom layer_hit_event, {:.2f}% remain".format(
            100 * len(self._select_bottom_layer_hit_event_index) / self._hit_array.shape[0]
        )) 

    # 2層連続でなっていないイベントを排除
    def _cut_non_2_layer_continue_event(self):
        self._cut_non_2_layer_continue_event_index = []
        for i_event in tqdm(self._select_bottom_layer_hit_event_index):
            for i_layer in range(8):
                if (i_layer == 7):
                    self._cut_non_2_layer_continue_event_index.append(i_event)
                if (np.all(self._layer_n_hit[i_event][i_layer:i_layer+1] == 0)):
                    break

        print("cut non 2 layer continue event is ",len(self._cut_non_2_layer_continue_event_index))
        print("selected select top & bottom layer_hit_event, {:.2f}% remain".format(
            100 * len(self._cut_non_2_layer_continue_event_index) / self._hit_array.shape[0]
        )) 

    # 3-7層で2hitあるイベントを保存
    def _select_2hits(self):
        self._select_2hits_index = [] 
        for i_event in tqdm(self._cut_non_2_layer_continue_event_index):
            if(np.any(self._layer_n_hit[i_event][1:6] >= 2)):
                self._select_2hits_index.append(i_event)
        print("select 2 hits event is ",len(self._select_2hits_index))
        print("selected 2 hits event, {:.2f}% remain".format(
            100 * len(self._select_2hits_index) / self._hit_array.shape[0]
        ))
    

    # 0,1層で2層が連続してhit
    def _select_top_layer_continue_hits_event (self):
        self._select_top_layer_continue_hits_event_index = []
        for i_event in tqdm(self._select_2hits_index):
            for i,j in itertools.product(range(4), range(4)):
                if (self._hit_array[i_event][6][i][j] == 1):
                    if(i == 0):
                        hit_slice = self._hit_array[i_event][7][0:i+2, j-1:j+2]
                        if(np.any(hit_slice == 1)):
                            self._select_top_layer_continue_hits_event_index.append(i_event)
                            break
                        continue
                    
                    if(j == 0):
                        hit_slice = self._hit_array[i_event][7][i-1:i+2, 0:j+2]
                        if(np.any(hit_slice == 1)):
                            self._select_top_layer_continue_hits_event_index.append(i_event)
                            break
                        continue
                    
                    else:
                        hit_slice = self._hit_array[i_event][7][i-1:i+2, j-1:j+2]
                        if(np.any(hit_slice == 1)):
                            self._select_top_layer_continue_hits_event_index.append(i_event)
                            break
                        continue

        print("0,1 layer continue hits event is ",len(self._select_top_layer_continue_hits_event_index))
        print("selected 0,1th layer continue hits event , {:.2f}% remain".format(
            100 * len(self._select_top_layer_continue_hits_event_index) / self._hit_array.shape[0]
        ))   
    
    # 3-7層でいずれかが2層連続してhit
    def _select_continue_2_hits(self):
        self._select_continue_2_hits_index = []
        for i_event in tqdm(self._select_top_layer_continue_hits_event_index):
            for i_layer, i,j in itertools.product(range(2,7), range(4), range(4)):    
                if (self._hit_array[i_event][i_layer][i][j] == 1):
                    if(i == 0):
                        hit_slice = self._hit_array[i_event][i_layer + 1][0:i+2, j-1:j+2]
                        if(np.any(hit_slice == 1)):
                            if (np.all(self._layer_n_hit[i_event][i_layer:i_layer+2] >= 2) ):
                                self._select_continue_2_hits_index.append(i_event)
                                break
                        continue
                    
                    if(j == 0):
                        hit_slice = self._hit_array[i_event][i_layer + 1][i-1:i+2, 0:j+2]
                        if(np.any(hit_slice == 1)):
                            if (np.all(self._layer_n_hit[i_event][i_layer:i_layer+2] >= 2) ):
                                self._select_continue_2_hits_index.append(i_event)
                                break
                        continue
                    
                    else:
                        hit_slice = self._hit_array[i_event][i_layer + 1][i-1:i+2, j-1:j+2]
                        if(np.any(hit_slice == 1)):
                            if (np.all(self._layer_n_hit[i_event][i_layer:i_layer+2] >= 2) ):
                                self._select_continue_2_hits_index.append(i_event)
                                break
                        continue
        
        print("all cut is ",len(self._select_continue_2_hits_index))
        print("selected all cut, {:.2f}% remain".format(
            100 * len(self._select_continue_2_hits_index) / self._hit_array.shape[0]
        ))   

    # 層の上と下でhitした菱形の中心値をとってくる
    def _get_fit_point(self, i_event):
        self._i_event = i_event
        self._top_layer = 7
        self._bottom_layer = 0

        # [i,j]で返される
        self._hit_top_point = np.where(self._hit_array[self._i_event][self._top_layer] == 1)
        self._hit_bottom_point = np.where(self._hit_array[self._i_event][self._bottom_layer] == 1)

        # [i]で返されるのでこの後にintに変える
        self._hit_top_i = self._hit_top_point[0]
        self._hit_top_j = self._hit_top_point[1]
        self._hit_bottom_i = self._hit_bottom_point[0]
        self._hit_bottom_j = self._hit_bottom_point[1]
        
        self._point_top = self.get_point(self._top_layer, self._hit_top_i[0], self._hit_top_j[0])
        self._point_bottom = self.get_point(self._bottom_layer, self._hit_bottom_i[0], self._hit_bottom_j[0])
        
        print("top:",self._point_top,"bottom:", self._point_bottom)

        # 5点以上必要だが2点しかフィットしないため無理やり6点を作る
        self._x = np.array([self._point_top[0],self._point_top[0],self._point_top[0],
                            self._point_bottom[0],self._point_bottom[0],self._point_bottom[0]])
        
        self._y = np.array([self._point_top[1],self._point_top[1],self._point_top[1],
                            self._point_bottom[1],self._point_bottom[1],self._point_bottom[1]])

        self._z = np.array([self._point_top[2],self._point_top[2],self._point_top[2],
                            self._point_bottom[2],self._point_bottom[2],self._point_bottom[2]])
        # ハイパーパラメータを初期化
        self._param = [0, 0, 0, 0, 0]
    
    # フィッティングする関数を作成
    def fiting_func(self,param,x,y,z):
        residual = z - (param[0]*x**2 + param[1]*y**2 + param[2]*x + param[3]*y + param[4])
        return residual

    # フィットした直線の方程式をとってくる
    def _get_fit_line_equition(self, i_event):
        x = np.array([self._point_top[0],self._point_top[0],self._point_top[0],
                            self._point_bottom[0],self._point_bottom[0],self._point_bottom[0]])
        y = np.array([self._point_top[1],self._point_top[1],self._point_top[1],
                            self._point_bottom[1],self._point_bottom[1],self._point_bottom[1]])
        z = np.array([self._point_top[2],self._point_top[2],self._point_top[2],
                            self._point_bottom[2],self._point_bottom[2],self._point_bottom[2]])

        # 最小二乗法を実装
        self._optimised_param =  optimize.leastsq(self.fiting_func, self._param, args=(x, y, z))

        print(self._optimised_param)

        # フィッティングする関数を求める
        self._a = self._optimised_param[0][0]
        self._b = self._optimised_param[0][1]
        self._c = self._optimised_param[0][2]
        self._d = self._optimised_param[0][3]
        self._e = self._optimised_param[0][4]

        print("a:",self._optimised_param[0][0])
        print("b:",self._optimised_param[0][1])
        print("c:",self._optimised_param[0][2])
        print("d:",self._optimised_param[0][3])
        print("e:",self._optimised_param[0][4])

        self._line_equition = self._a * self._x**2 + self._b * self._y**2 + self._c * self._x + self._d * self._y + self._e
        
    def write_fig(self, i_event):
        filename_short = self._rootfile_path.split('/')[-1]
        self._save_directory_path = "img_{}_{}_layer_hits_{}_hits_top_bottom_cut".format(filename_short, self._threshold_layer_number, self._threshold_hit)
        os.makedirs(self._save_directory_path, exist_ok=True)
        self._fig.write_image(self._save_directory_path + "/event{}.png".format(i_event), scale=10)
        print(self._save_directory_path + "/event{}.png".format(i_event))
        self._fig.write_html(self._save_directory_path + "/event{}.html".format(i_event))
        print(self._save_directory_path + "/event{}.html".format(i_event))