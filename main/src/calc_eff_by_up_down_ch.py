from pyroot_easiroc.EffCalculatorUpDown import EffCalculatorUpDown
from tqdm import tqdm
import multiprocessing
import ROOT as r
r.gROOT.SetBatch()


def calc_eff(adc):
    ec = EffCalculatorUpDown("tree", "/data/hamada/easiroc_data/run017_023.root")
    ec.set_ref_threshold_s([1100 for _ in range(64)])
    ec.set_threshold_s([adc for _ in range(64)])
    effs = ec.calc_all_ch_effeciency()
    return adc, effs


pool = multiprocessing.Pool(2)
adcs = list(range(800, 1500))
effeciency = []
with tqdm(total=len(adcs)) as t:
    for e in pool.imap_unordered(calc_eff, adcs):
        effeciency.append(e)
        t.update(1)

graphs = [r.TGraph() for _ in range(64)]
for ch in range(64):
    graphs[ch].SetMarkerStyle(8)
    graphs[ch].SetTitle("{}ch;ADC value;effeciency".format(ch))
    graphs[ch].GetYaxis().SetRangeUser(0, 1)
for e in effeciency:
    for ch in range(64):
        graphs[ch].SetPoint(graphs[ch].GetN(), e[0], e[1][ch])

canvas = r.TCanvas("c", "c", 1920*2, 1080*16)
canvas.Divide(4, 16)
for ch in range(64):
    canvas.cd(ch+1)
    graphs[ch].Draw("AP")
print("TCanvas save start . . .")
canvas.SaveAs("../img/calc_effeciency_updown.jpg")

print("TFile save start . . .")
tfile = r.TFile("../img/calc_effeciency_updown.root", "recreate")
tfile.cd()
for ch in range(64):
    graphs[ch].Write("graph_{}ch".format(ch))
