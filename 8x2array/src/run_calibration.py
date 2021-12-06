from pyroot_easiroc import calibrationUtils as util
import ROOT as r
r.gROOT.SetBatch()

json_path = "8x2array/json/cal_20211206_15_ch4.json"
util.getCalibrationParams(json_path)