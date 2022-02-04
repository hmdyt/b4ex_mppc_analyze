from pyroot_easiroc.MuonTrackReconstructor import MuonTrackReconstructor
from tqdm import tqdm

rootfile_path = "/data/hamada/easiroc_data/run017.root"
threshold_s = [1200] * 64

mtr = MuonTrackReconstructor(rootfile_path, threshold_s)
mtr._pre_cut_threshold_layer()
mtr._multi_hit()
mtr._under_layer_limit()
mtr.hit_muon_straight()

i_event = 0

mtr.show(mtr._hit_muon_index[i_event])