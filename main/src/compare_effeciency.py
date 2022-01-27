import numpy as np
from pyroot_easiroc.TrackSeeker import TrackSeeker
import ROOT as r
r.gROOT.SetBatch()

def get_eff(sigma_ratio):
    ts = TrackSeeker("tree", "run017.root")
    # set showing range, fit
    for ch in range(64):
        ts._hist[ch].GetXaxis().SetRangeUser(950, 4096)
        ts.fit_by_landau(ch)
    ts._hist[2].GetXaxis().SetRangeUser(1000, 4096)
    # set threshold
    for ch in range(64):
        MPV = ts._f_landau[ch].GetParameter(1)
        sigma = ts._f_landau[ch].GetParameter(2)
        ts.set_threshold(
            ch,
            int(MPV - sigma_ratio*sigma)
        )
    ts.set_threshold(33, 1000) # unko channel
    ts.determine_hit_by_landau_fit()
    for ch in ts.INNER_CHANNELS:
        ts.calc_effeciency(ch)
    return  ts._effeciency

if __name__ == "__main__":

    sigma_ratios = [0.5 * i for i in range(7)]
    sigma_ratios = np.linspace(0, 3, 50)
    effs = [get_eff(sigma_ratio) for sigma_ratio in sigma_ratios]

    graphs = [
        r.TGraph()
        for ch in range(64)
    ]
    canvas = r.TCanvas("c", "c", 1920*2, 1080*16)
    canvas.Divide(4, 16)
    for ch in range(64):
        canvas.cd(ch+1)
        i_point = 0
        for i, sigma_ratio in enumerate(sigma_ratios):
            if effs[i][ch] == None: continue
            graphs[ch].SetPoint(i_point, sigma_ratio, effs[i][ch])
            i_point += 1
        graphs[ch].SetMarkerStyle(8)
        graphs[ch].SetTitle("ch{};[1/sigma];effeciency".format(ch))
        graphs[ch].Draw("AP")
    canvas.SaveAs("compare_effeciency.png")