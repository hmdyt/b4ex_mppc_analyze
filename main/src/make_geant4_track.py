from pyroot_easiroc.MuonTrackReconstructor import MuonTrackReconstructor
from tqdm import tqdm

rootfile_path = "convertSimulationData.root"
threshold_s = [0.5] * 64

mtr = MuonTrackReconstructor(rootfile_path, threshold_s)
mtr._pre_cut_threshold_layer()
mtr._multi_hit()
mtr._under_layer_limit()
mtr.hit_muon_straight()

with open("make_geant4_track.txt", 'w') as f:
    for i_event in mtr._under_layer_limit_index:
        f.write("{}\n".format(i_event))

for i_event in tqdm(range(len(mtr._under_layer_limit_index)), desc="i_event"):
    mtr.show(mtr._under_layer_limit_index[i_event])
