import os
import json
import array
import ROOT as r
from copy import copy

# TGraph can using python list 
def TPGraphErrors(n, x, y, x_e, y_e):
    x = array.array('d', x)
    y = array.array('d', y)
    x_e = array.array('d', x_e)
    y_e = array.array('d', y_e)
    return r.TGraphErrors(n, x, y, x_e, y_e)

# .root => hist
def getHistMPPC(file_path, channel):
    file = r.TFile(file_path)
    hist = file.Get("ADC_HIGH_" + str(channel))
    hist.SetTitle(file_path.replace("data/cal_2021", "").replace(".root", "_") + str(channel) + "ch;ADC;Events")
    return copy(hist)

def searchPeaks(hist, peak_max, sigma=10):
    spectrum = r.TSpectrum(peak_max)
    spectrum.Search(hist, sigma, "new")
    x_peaks = spectrum.GetPositionX()
    y_peaks = spectrum.GetPositionY()
    n_peaks = int(spectrum.GetNPeaks())
    ret_x_peaks = [x_peaks[i] for i in range(n_peaks)]
    ret_y_peaks = [y_peaks[i] for i in range(n_peaks)]
    ret_x_peaks, ret_y_peaks = zip(*sorted(zip(ret_x_peaks, ret_y_peaks)))
    return n_peaks, ret_x_peaks, ret_y_peaks

# unko function
def getMultiGaussString(num):
    gausses_str = ""
    for i in range(num):
        gausses_str += "+gaus(" + str(3*i) + ")"
    return gausses_str

# fit sutego zaurusu
def getFittedParams(
    hist,
    peak_search_range = (0, 1500),
    fitting_range = (0, 1500),
    showing_range = (0, 1500),
    peak_search_sigma = 10
):
    # peak search
    hist.GetXaxis().SetRangeUser(*peak_search_range)
    n_peaks, x_peaks, y_peaks = searchPeaks(hist, 20, peak_search_sigma)
    multi_gauss_str = getMultiGaussString(n_peaks)

    # fitting
    f_fit = r.TF1("f", multi_gauss_str, *fitting_range)
    f_fit.SetNpx(10000)
    for i in range(n_peaks):
        f_fit.SetParName(3*i + 0, str(i) + "th const")
        f_fit.SetParName(3*i + 1, str(i) + "th mean")
        f_fit.SetParName(3*i + 2, str(i) + "th sigma")
        f_fit.SetParameter(3*i + 0, y_peaks[i])
        f_fit.SetParameter(3*i + 1, x_peaks[i])
        f_fit.SetParameter(3*i + 2, 5)
        f_fit.SetParLimits(3*i + 0, 0, 10**6)
        f_fit.SetParLimits(3*1 + 2, 0, 100)
    hist.Fit(f_fit, "R")

    # set showing range
    hist.GetXaxis().SetRangeUser(*showing_range)
    
    # return
    ret_adc_means = [f_fit.GetParameter(3*i + 1) for i in range(n_peaks)]
    ret_adc_mean_errors = [f_fit.GetParError(3*i + 1) for i in range(n_peaks)]
    return ret_adc_means, ret_adc_mean_errors

# make calibration line
# it returns pol1 params
def getCalibrationParams(
    json_file_path = "/home/hamada/b4ex/ensoku/json/cal_20211112_16_36.json",
):  
    # fetch json, hist
    settings = json.load(open(json_file_path))
    title = settings["root_file_path"] + " " + str(settings["target_channel"])
    peak_search_sigma = settings.get("peak_search_sigma", 10)
    hist = getHistMPPC(settings["root_file_path"], settings["target_channel"])

    # prepare dir
    os.makedirs(settings["image_save_path"], exist_ok=True)
    
    # fetch fitting params
    adc_means, adc_mean_errors = getFittedParams(
        hist,
        settings["peak_search_range"],
        settings["fitting_range"],
        settings["showing_range"],
        peak_search_sigma
    )

    # init graph
    n_points = len(adc_means)
    photon_nums = [settings["initial_photon_num"] + i for i in range(n_points)]
    photon_num_errors = [0 for _ in range(n_points)]
    g = TPGraphErrors(n_points, photon_nums, adc_means, photon_num_errors, adc_mean_errors)
    g.SetTitle(title + ";Photon Number;ADC Value")
    g.SetMarkerStyle(8)
    g.SetMarkerSize(1)
    
    # init liner function for fitting and fit
    f_fit = r.TF1("f_liner", "[0]*x + [1]", 0, 20)
    g.Fit(f_fit, "R")
    
    # init axis for Tgraph
    photon_num_range = (0, photon_nums[-1] + 1)
    adc_range = tuple(map(f_fit.Eval, photon_num_range))
    axis = r.TH2D(
        "axis", title + ";Photon Number;ADC Value",
        0, *photon_num_range,
        0, *adc_range
        )
    axis.SetStats(0)
    
    # save image
    c1 = r.TCanvas()
    hist.Draw()
    c1.SaveAs(settings["image_save_path"] + "hist.png")
    c2 = r.TCanvas()
    axis.Draw("AXIS")
    g.Draw("P SAME")
    c2.SaveAs(settings["image_save_path"] + "graph.png")
    
    # return
    # y   = ax         + b
    # ADC = a * Photon + b
    a, b = f_fit.GetParameter(0), f_fit.GetParameter(1)
    return a, b
