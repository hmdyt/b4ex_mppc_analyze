from pyroot_easiroc import ExtendedTTree
from pyroot_easiroc import calibrationUtils as util
import ROOT as r
r.gROOT.SetBatch()


# TODO: fix truth value
HIGH_VOLTAGE_VALUES = [52.2, 52.4, 52.6, 52.8]
ROOT_FILES = [
    "/data/hamada/easiroc_data/test_20211225_11.root",
    "/data/hamada/easiroc_data/test_20211225_12.root",
    "/data/hamada/easiroc_data/test_20211225_13.root",
    "/data/hamada/easiroc_data/test_20211225_14.root"
]

trees = [ExtendedTTree.ExtendedTTree("tree", "", ROOT_FILES[i]) for i in range(4)]

# fit
for file_no in range(4):
    for ch in range(64):
        trees[file_no].fit_pedestal_auto_range(ch)


def make_graph(ch):
    x_pedestal = [
        trees[0].get_pedestal_fit_params(ch)["mean"][0],
        trees[1].get_pedestal_fit_params(ch)["mean"][0],
        trees[2].get_pedestal_fit_params(ch)["mean"][0],
        trees[3].get_pedestal_fit_params(ch)["mean"][0]
    ]
    x_pedestal_error = [
        trees[0].get_pedestal_fit_params(ch)["mean"][1],
        trees[1].get_pedestal_fit_params(ch)["mean"][1],
        trees[2].get_pedestal_fit_params(ch)["mean"][1],
        trees[3].get_pedestal_fit_params(ch)["mean"][1]
    ]
    graph = util.TPGraphErrors(4, x_pedestal, HIGH_VOLTAGE_VALUES, x_pedestal_error, [0,0,0,0])
    func = r.TF1("", "[0]*x+[1]", min(x_pedestal), max(x_pedestal))
    graph.Fit(func, "R")
    canvas = r.TCanvas()
    graph.Draw("AP")
    canvas.SaveAs("./{}.png".format(ch))
    return func.GetParameter(0), func.GetParameter(1)


for ch in range(64):
    make_graph(ch)