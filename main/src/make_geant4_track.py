from pyroot_easiroc.FitPointMuonTrackReconstructor import FitPointMuonTrackReconstructor
from tqdm import tqdm

rootfile_path = "/data/hamada/simulation_data/convertSimulationData_09.root"
threshold_s = [0.5] * 64

fpmtr = FitPointMuonTrackReconstructor(rootfile_path, threshold_s)
fpmtr._pre_cut_threshold_layer()
fpmtr._select_top_layer_hit_event()
fpmtr._select_bottom_layer_hit_event()
fpmtr._cut_non_2_layer_continue_event()
fpmtr._select_2hits()
fpmtr._select_top_layer_continue_hits_event()
fpmtr._select_continue_2_hits()

with open("make_geant4_track.txt", 'w') as f:
    for i_event in fpmtr._select_continue_2_hits_index:
        f.write("{}\n".format(i_event))
