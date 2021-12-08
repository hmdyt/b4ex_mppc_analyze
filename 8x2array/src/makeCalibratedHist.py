from pyroot_easiroc import calibrationUtils as util
import ROOT as r
r.gROOT.SetBatch()

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

# cosmic ray mesurement file
target_file = "/data/hamada/easiroc_data/test_20211207_2_*.root"
chain = r.TChain("tree")
chain.Add(target_file)

# fetch calb parameters
# calb_paras = {ch: [a, b]}
# ADC = a * N_photon + b
calibration_functions = dict()
for up_down in ["downside", "upside"]:
    for ch in channels[up_down]:
        a, b = util.getCalibrationParams("8x2array/json/" + json_names[up_down].format(ch))
        f = lambda x: (x - b) / a
        calibration_functions[ch] = f

# draw & save combined hist
hist_downside = r.TH1D("hist", ";Photon Number;Events", 1024, 1, 70)
for i_event in range(chain.GetEntries()):
    chain.GetEntry(i_event)
    for up_down in ["downside"]:
        for ch in channels[up_down]:
            hist_downside.Fill(calibration_functions[ch](chain.VadcHigh[ch]))
c = r.TCanvas()
hist_downside.Draw()
c.SaveAs("8x2array/img/test_20211207_2_*/combined_downside.png")

hist_upside = r.TH1D("hist", ";Photon Number;Events", 1024, 1, 70)
for i_event in range(chain.GetEntries()):
    chain.GetEntry(i_event)
    for up_down in ["upside"]:
        for ch in channels[up_down]:
            hist_upside.Fill(calibration_functions[ch](chain.VadcHigh[ch]))
c = r.TCanvas()
hist_upside.Draw()
c.SaveAs("8x2array/img/test_20211207_2_*/combined_upside.png")

# draw & save separated hist
hists = dict()
canvases = dict()
for up_down in ["downside", "upside"]:
    for ch in channels[up_down]:
        hists[ch] = r.TH1D("", "test_20211207_2_* {0}ch;Photon Number;Events".format(ch), 1024, 1, 70)
        canvases[ch] = r.TCanvas()
        for i_event in range(chain.GetEntries()):
            chain.GetEntry(i_event)
            hists[ch].Fill(calibration_functions[ch](chain.VadcHigh[ch]))
        hists[ch].Draw()
        canvases[ch].SaveAs("8x2array/img/test_20211207_2_*/ch{0}.png".format(ch))