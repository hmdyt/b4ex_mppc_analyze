from pyroot_easiroc import calibrationUtils as util
import ROOT as r
r.gROOT.SetBatch()

json_paths = []

for ch in range(4, 12):
    json_path = "8x2array/json/cal_20211206_14_ch{0}.json".format(ch)
    json_paths.append(json_path)
    
for ch in range(20, 28):
    json_path = "8x2array/json/cal_20211206_21_ch{0}.json".format(ch)
    json_paths.append(json_path)

for json_path in json_paths:
    util.getCalibrationParams(json_path)