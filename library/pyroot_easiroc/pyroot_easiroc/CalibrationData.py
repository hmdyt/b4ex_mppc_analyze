from typing import List, Dict
import ROOT as r
from tqdm import tqdm
from . import calibrationUtils as util
import os


class CalibrationData:

    def __init__(self, image_dir_path: str, MPPC_high_voltage: str) -> None:
        self._image_dir_path: str = image_dir_path
        self._HV: str = MPPC_high_voltage
        self._hists_VadcHigh: List[r.TH1D] = [None for _ in range(64)]
        self._fitted_adc_means: List[List[float]] = [None for _ in range(64)]
        self._fitted_adc_mean_errors: List[List[float]] = [None for _ in range(64)]

    def set_hist(self, detector_ch: int, cal_root_file_path: str, cal_ch: int) -> None:
        hist = util.getHistMPPC(cal_root_file_path, cal_ch)
        hist.SetTitle("{0} [{1}ch];ADC;Events".format(cal_root_file_path.split('/')[-1], detector_ch))
        self._hists_VadcHigh[detector_ch] = hist

    def fit_multi_gaus(
        self,
        ch,
        peak_search_range=(0, 1500),
        fitting_range=(0, 1500),
        peak_search_sigma=10
    ) -> None:
        hist = self._hists_VadcHigh[ch]
        # determine hist showing range
        xmin = 0
        xmax = 4096
        while self._hists_VadcHigh[ch].GetBinContent(xmin) == 0:
            xmin += 1
        while self._hists_VadcHigh[ch].GetBinContent(xmax) == 0:
            xmax -= 1
        # fit
        ret_adc_means, ret_adc_mean_errors = util.getFittedParams(
            hist,
            peak_search_range,
            fitting_range,
            (xmin, xmax),
            peak_search_sigma
        )
        # set to member variable & save hist as image
        self._fitted_adc_means[ch] = ret_adc_means
        self._fitted_adc_mean_errors[ch] = ret_adc_mean_errors
        self.save_hist_as_png(ch)

    def save_hist_as_png(self, ch):
        canvas = r.TCanvas()
        self._hists_VadcHigh[ch].Draw()
        canvas.SaveAs("{0}/{1}/hist.png".format(self._image_dir_path, ch))


class CalibrationDatas:

    def __init__(self) -> None:
        self._calbDatas: Dict[str, CalibrationData] = {}
        self._HVs: List[str] = []
        self._calb_line_TGraphs: Dict[str, List[r.TGraphErrors]] = {}
        self._calb_line_TF1s: Dict[str, List[r.TF1]] = {}
        self._calb_line_TCanvases: Dict[str, List[r.TCanvas]] = {}
        self._HV_one_photon_TGraphs: List[r.TGraphErrors] = [None for _ in range(64)]
        self._HV_one_photon_TF1s: List[r.TF1] = [None for _ in range(64)]
        self._pedestal_data_path: str = None
        self._pedestal_adc_means: List[float] = [None for _ in range(64)]
        self._pedestal_adc_mean_errors: List[float] = [None for _ in range(64)]
        self._initial_photon_number_s: Dict[str, List[int]] = {}

    def set_calb_data(self, img_dir_path: str, HV: str) -> None:
        self._calbDatas[HV] = CalibrationData(img_dir_path, HV)
        self._HVs.append(HV)
        self._calb_line_TCanvases[HV] = [None for _ in range(64)]
        self._calb_line_TGraphs[HV] = [None for _ in range(64)]
        self._calb_line_TF1s[HV] = [None for _ in range(64)]
        self._initial_photon_number_s[HV] = [None for _ in range(64)]
        self.make_dirs()

    def get_calb_data(self, HV: str) -> CalibrationData:
        return self._calbDatas[HV]

    def fit_adc_nphoton_line(self, HV, ch, initial_photon_num):
        # init graph
        n_points = len(self._calbDatas[HV]._fitted_adc_means[ch])
        photon_nums = [initial_photon_num + i for i in range(n_points)]
        photon_num_errors = [0 for _ in range(n_points)]
        adc_means = self._calbDatas[HV]._fitted_adc_means[ch]
        adc_mean_errors = self._calbDatas[HV]._fitted_adc_mean_errors[ch]
        graph = util.TPGraphErrors(
            n_points,
            photon_nums,
            adc_means,
            photon_num_errors,
            adc_mean_errors
        )
        graph.SetTitle("{}ch;Photon Number;ADC Value".format(ch))
        graph.SetMarkerStyle(8)
        graph.SetMarkerSize(1)

        # init liner function for fitting and fit
        f_fit = r.TF1("f_liner", "[0]*x + [1]", 0, 20)
        graph.Fit(f_fit, "R")

        # init axis for Tgraph
        photon_num_range = (0, photon_nums[-1] + 1)
        adc_range = tuple(map(f_fit.Eval, photon_num_range))
        axis = r.TH2D(
            "axis", "{}ch;Photon Number;ADC Value".format(ch),
            0, *photon_num_range,
            0, *adc_range
        )
        axis.SetStats(0)

        # draw to canvas
        canvas = r.TCanvas()
        axis.Draw("AXIS")
        graph.Draw("P SAME")

        # set to member function & save canvas as png
        self._calb_line_TCanvases[HV][ch] = canvas
        self._calb_line_TGraphs[HV][ch] = graph
        self._calb_line_TF1s[HV][ch] = f_fit
        self.save_calb_line_TCanvas(HV, ch)

    def fit_all_adc_nphoton_line(self):
        for HV in self._HVs:
            for ch in range(64):
                initial_photon_num = self._initial_photon_number_s[HV][ch]
                self.fit_adc_nphoton_line(HV, ch, initial_photon_num)

    def save_calb_line_TCanvas(self, HV, ch):
        save_str = "{0}/{1}/graph_photon_adc.png".format(
            self._calbDatas[HV]._image_dir_path,
            ch
        )
        self._calb_line_TCanvases[HV][ch].SaveAs(save_str)

    def fit_HV_one_photon(self, ch):
        # fetch graph attr
        n_points = len(self._HVs)
        HVs = []
        HV_errors = []
        one_photon_adc_widthes = []
        one_photon_adc_width_errors = []
        for HV in self._HVs:
            HVs.append(float(HV))
            one_photon_adc_widthes.append(
                self._calb_line_TF1s[HV][ch].GetParameter(0)
            )
            HV_errors.append(0)
            one_photon_adc_width_errors.append(
                self._calb_line_TF1s[HV][ch].GetParError(0)
            )

        # init graph
        graph = util.TPGraphErrors(
            n_points,
            HVs,
            one_photon_adc_widthes,
            HV_errors,
            one_photon_adc_width_errors
        )
        graph.SetTitle("{}ch;MPPC HV [V];ADC/One Photon".format(ch))
        graph.SetMarkerStyle(8)
        graph.SetMarkerSize(1)

        # init liner function for fitting and fit
        f_fit = r.TF1("f_liner", "[0]*x + [1]", 0, 60)
        graph.Fit(f_fit, "R")

        # set to class member variable & save graph as png
        self._HV_one_photon_TGraphs[ch] = graph
        self._HV_one_photon_TF1s[ch] = f_fit
        self.save_HV_one_photon_TGraph(ch)

    def save_HV_one_photon_TGraph(self, ch):
        save_str = "{0}/{1}/HV_one_photon_TGraph.png"
        canvas = r.TCanvas()
        self._HV_one_photon_TGraphs[ch].Draw("AP")
        for HV in self._HVs:
            canvas.SaveAs(save_str.format(self._calbDatas[HV]._image_dir_path, ch))

    def make_dirs(self):
        for HV in self._HVs:
            os.makedirs(self._calbDatas[HV]._image_dir_path, exist_ok=True)
            for i in range(64):
                os.makedirs("{0}/{1}".format(self._calbDatas[HV]._image_dir_path, i), exist_ok=True)

    def set_pedestal_data(self, pedestal_data_path):
        self._pedestal_data_path = pedestal_data_path
        hists = [util.getHistMPPC(self._pedestal_data_path, ch) for ch in range(64)]
        funcs = [r.TF1("", "gaus", 0, 4096) for _ in range(64)]
        for ch in range(64):
            hists[ch].Fit(funcs[ch], "R")
            self._pedestal_adc_means[ch] = funcs[ch].GetParameter(1)
            self._pedestal_adc_mean_errors[ch] = funcs[ch].GetParError(1)

    def determine_initial_photon_number(self, HV, ch):
        fitted_means = self._calbDatas[HV]._fitted_adc_means[ch]
        pedestal_mean = self._pedestal_adc_means[ch]
        diff_ped_to_ini = fitted_means[0] - pedestal_mean
        aprox_width = fitted_means[1] - fitted_means[0]
        initial_photon_number = round(diff_ped_to_ini / aprox_width)
        self._initial_photon_number_s[HV][ch] = initial_photon_number

    def determine_all_initial_photon_number(self):
        for HV in self._HVs:
            for ch in range(64):
                self.determine_initial_photon_number(HV, ch)

    def print_fitted_pedestal(self):
        for HV in self._HVs:
            print("========== {}V ==========".format(HV))
            for ch in range(64):
                print(self._calb_line_TF1s[HV][ch].Eval(0))

    def get_HV_from_one_photon(self, ch, one_photon_width) -> float:
        a = self._HV_one_photon_TF1s[ch].GetParameter(0)
        b = self._HV_one_photon_TF1s[ch].GetParameter(1)
        return (one_photon_width - b) / a
