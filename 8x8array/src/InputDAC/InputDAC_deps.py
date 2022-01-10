import json
from typing import Dict, List
import plotly.graph_objects as go
import sys
from tqdm import tqdm
from pprint import pprint


def load_file(file_path: str = "/data/hamada/easiroc_data/InputDAC_mesurement/01.json") -> Dict[str, list]:
    return json.load(open(file_path, 'r'))


def show_a_figure(data_list: Dict[float, List[List[List[float]]]], setHV: int, ch: int) -> None:
    fig = go.Figure(
        data=go.Scatter(
            x=data_list[setHV][ch][0],
            y=data_list[setHV][ch][1]
        ),
        layout=go.Layout(
            title=dict(text="InputDAC_Value - DAC_Voltage (setHV {}V, {}ch)".format(setHV, ch)),
            xaxis=dict(title='Input DAC Value (256 ~ 511)'),
            yaxis=dict(title='DAC Voltage [V]')
        )
    )
    fig.update_traces(mode="lines+markers", selector=dict(type='scatter'))
    fig.show()


if __name__ == "__main__":
    d1 = load_file("/data/hamada/easiroc_data/InputDAC_mesurement/01.json")
    d2 = load_file("/data/hamada/easiroc_data/InputDAC_mesurement/02.json")
    # setHV, realHV, DAC_value, DAC_HVs
    d1["data"].pop(0)
    d2["data"].pop(0)
    setHV_list: List[float] = list(set([float(v[0]) for v in d1['data']])) + list(set([float(v[0]) for v in d2['data']]))
    data_list: Dict[float, List[List[List[float]]]] = {realHV: [[[], []] for _ in range(64)] for realHV in setHV_list}

    for v in d1["data"] + d2["data"]:
        setHV: int = int(v[0])
        realHV: float = float(v[1])
        DAC_value: int = int(v[2])
        DAC_HVs: List[float] = list(map(float, v[3]))
        for ch in range(64):
            data_list[setHV][ch][0].append(DAC_value)
            data_list[setHV][ch][1].append(DAC_HVs[ch])

    if len(sys.argv) == 3:
        show_a_figure(data_list, int(sys.argv[1]), int(sys.argv[2]))
        exit()

    for ch in tqdm(range(64)):
        plotly_data = [
            go.Scatter(x=data_list[setHV][ch][0], y=data_list[setHV][ch][1], name="{}V".format(setHV))
            for setHV in setHV_list
        ]
        plotly_layout = go.Layout(
            title=dict(text="InputDAC_Value - DAC_Voltage ({}ch)".format(ch)),
            xaxis=dict(title='Input DAC Value (256 ~ 511)'),
            yaxis=dict(title='DAC Voltage [V]')
        )
        fig = go.Figure(data=plotly_data, layout=plotly_layout)
        fig.update_traces(mode="lines", selector=dict(type='scatter'))
        fig.write_html('InputDAC_deps_html/ch{}.html'.format(ch))
