from pyroot_easiroc.FitPointMuonTrackReconstructor import FitPointMuonTrackReconstructor
from pyroot_easiroc.LayerVisualizer import LayerVisualizer
from tqdm import tqdm

rootfile_path = "/data/hamada/easiroc_data/run017.root"
threshold_s = [1200] * 64

fpmtr = FitPointMuonTrackReconstructor(rootfile_path, threshold_s)

# cut event
fpmtr._pre_cut_threshold_layer()
fpmtr._select_top_layer_hit_event()
fpmtr._select_bottom_layer_hit_event()
fpmtr._cut_non_2_layer_continue_event()
fpmtr._select_2hits()
fpmtr._select_top_layer_continue_hits_event()
fpmtr._select_continue_2_hits()

# fit 
for i_event in tqdm(range(len(fpmtr._select_continue_2_hits_index))):
    fpmtr._get_fit_point(fpmtr._select_continue_2_hits_index[i_event])
    fpmtr.fiting_func(fpmtr._param, fpmtr._x, fpmtr._y, fpmtr._z)
    fpmtr._get_fit_line_equition(fpmtr._select_continue_2_hits_index[i_event])
    fpmtr._init_fig()
    fpmtr.draw_mesh(fpmtr._select_continue_2_hits_index[i_event])
    fpmtr.draw_line([fpmtr._point_top[0], fpmtr._point_top[1], fpmtr._point_top[2]], [fpmtr._point_bottom[0], fpmtr._point_bottom[1], fpmtr._point_bottom[2]])
    fpmtr.write_fig(fpmtr._select_continue_2_hits_index[i_event])
    LayerVisualizer(fpmtr).write_fig()