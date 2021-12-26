from typing import List, Dict
import ROOT as r
from tqdm import tqdm
from . import calibrationUtils as util
import os


class CalibrationData:
    _HV: str = None
    _image_dir_path: str = ""
    _hists_VadcHigh: List[r.TH1D] = [None for _ in range(64)]
    _fitted_adc_means: List[List[float]] = [None for _ in range(64)]
    _fitted_adc_mean_errors: List[List[float]] = [None for _ in range(64)]

    def __init__(self, image_dir_path: str, MPPC_high_voltage: str) -> None:
        self._image_dir_path = image_dir_path
        self._HV = MPPC_high_voltage

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
    _calbDatas: Dict[str, CalibrationData] = {}
    _HVs: List[str] = []
    _calb_line_TGraphs: Dict[str, List[r.TGraphErrors]] = {}
    _calb_line_TF1s: Dict[str, List[r.TF1]] = {}
    _calb_line_TCanvases: Dict[str, List[r.TCanvas]] = {}
    _HV_one_photon_TGraphs: List[r.TGraphErrors] = [None for _ in range(64)]
    _HV_one_photon_TF1s: List[r.TF1] = [None for _ in range(64)]

    def __init__(self) -> None:
        pass

    def set_calb_data(self, img_dir_path: str, HV: float) -> None:
        calbData: CalibrationData = CalibrationData(img_dir_path, HV)
        self._calbDatas[HV] = calbData
        self._HVs.append(HV)
        self._calb_line_TCanvases[HV] = [None for _ in range(64)]
        self._calb_line_TF1s[HV] = [None for _ in range(64)]
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
        self._calb_line_TF1s[HV][ch] = f_fit
        self.save_calb_line_TCanvas(HV, ch)

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
            HV = float(HV)
            HVs.append(HV)
            one_photon_adc_widthes.append(
                self._calb_line_TF1s[ch].GetParameter(0)
            )
            HV_errors.append(0)
            one_photon_adc_width_errors.append(
                self._calb_line_TF1s[ch].GetParError(0)
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
        f_fit = r.TF1("f_liner", "[0]*x + [1]", 0, 20)
        graph.Fit(f_fit, "R")

        # set to class member variable & save graph as png
        self._HV_one_photon_TGraphs[ch] = graph
        self._HV_one_photon_TF1s = f_fit
        self.save_HV_one_photon_TGraph(ch)

    def save_HV_one_photon_TGraph(self, ch):
        save_str = "{0}/{1}/HV_one_photon_TGraph.png"
        canvas = r.TCanvas()
        self._HV_one_photon_TGraphs[ch].Draw("AP")
        for HV in self._HVs:
            canvas.SaveAs(save_str.format(HV, ch))

    def make_dirs(self):
        for HV in self._HVs:
            os.makedirs(self._calbDatas[HV]._image_dir_path, exist_ok=True)
            for i in range(64):
                os.makedirs("{0}/{1}".format(self._calbDatas[HV]._image_dir_path, i), exist_ok=True)
