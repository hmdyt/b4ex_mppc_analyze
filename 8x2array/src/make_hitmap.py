from pyroot_easiroc import calibrationUtils as util
import ROOT as r
import numpy as np
from tqdm import tqdm
import sys
r.gROOT.SetBatch()

def fetch_calibration_functions():
    # available ch
    # up side   20 ~ 27
    # down side 4  ~ 11
    channels = dict()
    channels["downside"] = [i for i in range(4, 12)]
    channels["upside"] = [i for i in range(20, 28)]

    # json file name
    json_names = dict()
    json_names["downside"] = "cal_20211206_14_ch{0}.json"
    json_names["upside"] = "cal_20211206_21_ch{0}.json"

    # MPPC 52.33V
    calib_files = dict()
    calib_files["downside"] = "/data/hamada/easiroc_data/cal_20211206_14.root"
    calib_files["upside"] = "/data/hamada/easiroc_data/cal_20211206_21.root"

    # fetch calb parameters
    # calb_paras = {ch: [a, b]}
    # ADC = a * N_photon + b
    calibration_functions = dict()
    for up_down in ["downside", "upside"]:
        for ch in channels[up_down]:
            a, b = util.getCalibrationParams("8x2array/json/" + json_names[up_down].format(ch))
            f = lambda x: (x - b) / a
            calibration_functions[ch] = f
    return calibration_functions, channels

def is_scintillated(photon_number, threshold_photon_number):
    return float(photon_number > threshold_photon_number)

def main():
    THRESHOLD = int(sys.argv[1])
    
    calibration_functions, channels = fetch_calibration_functions()
    
    # cosmic ray mesurement file
    target_file = "/data/hamada/easiroc_data/test_20211207_2_*.root"
    chain = r.TChain("tree")
    chain.Add(target_file)
    
    crossed_accumrated_map = np.array([[0. for _ in range(8)] for _ in range(8)])
    
    for i_event in tqdm(range(chain.GetEntries())):
        chain.GetEntry(i_event)
        upside_map = np.array([[
            is_scintillated(calibration_functions[i](chain.VadcHigh[i]), THRESHOLD)
            for i in channels["upside"]
            ] for _ in range(8)])
        downside_map = np.array([[
            is_scintillated(calibration_functions[i](chain.VadcHigh[i]), THRESHOLD)
            for i in channels["downside"]
            ] for _ in range(8)])
        crossed_map = upside_map * downside_map.T
        if np.sum(crossed_map) == 0: continue
        crossed_map = crossed_map / np.sum(crossed_map)
        crossed_accumrated_map += crossed_map
    #crossed_accumrated_map = np.flipud(crossed_accumrated_map)
    crossed_accumrated_map = np.fliplr(crossed_accumrated_map)
    
    hist_hitmap = r.TH2D("hist_hitmap",
                        "test_20211207_2_* threshold{0} {1} events;ch (upside);ch (downside)".format(THRESHOLD, int(np.sum(crossed_accumrated_map))),
                        8, 0 + 0.5, 8 + 0.5,
                        8, 0 + 0.5, 8 + 0.5
                        )
    for i in range(1, 9): hist_hitmap.GetXaxis().SetBinLabel(i, str(28 - i))
    for i in range(1, 9): hist_hitmap.GetYaxis().SetBinLabel(i, str(3 + i))
    for i in range(8):
        for j in range(8):
            hist_hitmap.SetBinContent(i+1, j+1, crossed_accumrated_map[j][i])
            
    canvas = r.TCanvas()
    drawoption = "lego"
    hist_hitmap.Draw(drawoption)
    r.gStyle.SetOptStat(0)
    canvas.SaveAs("8x2array/img/test_20211207_2_*/hitmap_threshold{0}_{1}.png".format(THRESHOLD, drawoption))
    

if __name__ == "__main__":
    main()