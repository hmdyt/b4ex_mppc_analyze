from pyroot_easiroc.EffCalculator import EffCalculator
import pickle
import sys
import ROOT as r
from tqdm import tqdm
r.gROOT.SetBatch()

n_hit = int(sys.argv[1])
ec = EffCalculator(n_hit, "tree", "/data/hamada/easiroc_data/run017_021.root")

graphs = [r.TGraph() for _ in range(64)]
for ch in range(64):
    graphs[ch].SetMarkerStyle(8)
    graphs[ch].SetTitle("{}ch n={};ADC value;effeciency".format(ch, n_hit))

for adc in tqdm(range(900, 1500), desc="entire"):
    ec.determine_hits([adc for _ in range(64)])
    eff_s = ec.get_64ch_effeciency()
    for ch in range(64):
        graphs[ch].SetPoint(graphs[ch].GetN(), adc, eff_s[ch])

canvas = r.TCanvas("c", "c", 1920*2, 1080*16)
canvas.Divide(4, 16)
for ch in range(64):
    canvas.cd(ch+1)
    graphs[ch].Draw("AP")
print("TCanvas save start . . .")
canvas.SaveAs("../img/compare_effeciency_by_pedestal_n_{}.jpg".format(n_hit))

print("TFile save start . . .")
tfile = r.TFile("../img/compare_effeciency_by_pedestal_n_{}.root", "recreate")
tfile.cd()
for ch in range(64):
    graphs[ch].Write("graph_{}ch".format(ch))
