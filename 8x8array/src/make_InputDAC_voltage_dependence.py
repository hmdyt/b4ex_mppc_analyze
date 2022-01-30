from typing import Dict, List
import json

import ROOT as r


def load_file(file_path: str = "/data/hamada/easiroc_data/InputDAC_mesurement/01.json") -> Dict[str, list]:
    return json.load(open(file_path, 'r'))


def make_data(
    filepath1: str = "/data/hamada/easiroc_data/InputDAC_mesurement/01.json",
    filepath2: str = "/data/hamada/easiroc_data/InputDAC_mesurement/02.json"
):
    d1 = load_file("/data/hamada/easiroc_data/InputDAC_mesurement/01.json")
    d2 = load_file("/data/hamada/easiroc_data/InputDAC_mesurement/02.json")
    # setHV, realHV, DAC_value, DAC_HVs
    d1["data"].pop(0)
    d2["data"].pop(0)
    setHV_list: List[float] = list(set([float(v[0]) for v in d1['data']])) + list(set([float(v[0]) for v in d2['data']]))
    data_list: Dict[float, List[List[List[float]]]] = {setHV: [[[], []] for _ in range(64)] for setHV in setHV_list}
    setHV_to_realHV: Dict[float, float] = {setHV: 0. for setHV in setHV_list}
    setHV_to_realHV_list: Dict[float, List[float]] = {setHV: [] for setHV in setHV_list}

    for v in d1["data"] + d2["data"]:
        setHV: int = int(v[0])
        realHV: float = float(v[1])
        DAC_value: int = int(v[2])
        DAC_HVs: List[float] = list(map(float, v[3]))
        setHV_to_realHV_list[setHV].append(realHV)
        for ch in range(64):
            data_list[setHV][ch][0].append(DAC_value)
            data_list[setHV][ch][1].append(DAC_HVs[ch])
        for k, v in setHV_to_realHV_list.items():
            setHV_to_realHV[setHV] = sum(setHV_to_realHV_list[setHV]) / len(setHV_to_realHV_list[setHV])
    return data_list, setHV_to_realHV


if __name__ == "__main__":
    r.gROOT.SetBatch()
    data_list, setHV_to_realHV = make_data()
    canvas = r.TCanvas("c", "c", 1920*2, 1080*16)
    canvas.Divide(4, 16)
    TGraphs = [r.TGraph() for _ in range(64)]
    TGraph_indexs = [0 for _ in range(64)]
    TF1s = [r.TF1("f{}".format(i), "[0]*x+[1]", 2, 400) for i in range(64)]
    for HV in data_list.keys():
        for ch in range(64):
            for i in range(len(data_list[HV][ch][0])):
                # remove unko data
                if ch == 37 and (4.49 < data_list[HV][ch][1][i]):
                    continue
                TGraphs[ch].SetPoint(
                    TGraph_indexs[ch],
                    data_list[HV][ch][0][i],
                    data_list[HV][ch][1][i]
                )
                TGraph_indexs[ch] += 1

    file = open("InputDAC_voltage_dependence", 'w')
    for i, (f, g) in enumerate(zip(TF1s, TGraphs)):
        canvas.cd(i+1)
        g.SetTitle("ch{};InputDAC_value;InputDAC_voltage[V]".format(i))
        g.Fit(f, "R")
        g.Draw("AP")
        s = "{} {} {}\n".format(i, f.GetParameter(0), f.GetParameter(1))
        file.write(s)
    canvas.SaveAs("InputDAC_fit_root.png")

    """
    cds = CalibrationData.CalibrationDatas()
    cds.set_InputDAC_mesurement_data(data_list)
    cds.set_setHV_to_realHV(setHV_to_realHV)
    cds.fit_InputDAC_vaule_voltage_line(53, 0)
    """
