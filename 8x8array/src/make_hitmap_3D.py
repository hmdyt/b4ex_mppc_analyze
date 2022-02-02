import numpy as np
import ROOT as r
import numpy as np
import sys
import os

import plotly.graph_objects as go
from make_rhombus import Rhombus
from plotly.subplots import make_subplots
r.gROOT.SetBatch()


def is_scintillated(adc_value, threshold_adc_value):
    return float(adc_value > threshold_adc_value)


def make_crossed_map(threshold, i_event, layar, filename):

    # cosmic ray mesurement file
    target_file = filename
    chain = r.TChain("tree")
    chain.Add(target_file)
    chain.GetEntry(i_event)

    # downside 0 ~ 3 , 4 ~ 7 ...
    # upside 60 ~ 63, 56 ~ 59 ...
    channels = dict()
    channels["downside"] = [i for i in range(0 + (4 * layar), 4 + (4 * layar))]
    channels["upside"] = [i for i in range(60 - (4 * layar), 64 - (4 * layar))]

    upside_map = np.array([[
        is_scintillated(chain.VadcHigh[i], threshold)
        for i in channels["upside"]
    ]] * 4)

    downside_map = np.array([[
        is_scintillated(chain.VadcHigh[i], threshold)
        for i in channels["downside"]
    ]] * 4)
    crossed_map = upside_map * downside_map.T
    crossed_map = crossed_map.T
    return crossed_map


def save_hitmap_as_html_png(threshold, i_event, filename):
    hitmap_3d = []
    for layar in range(8):
        crossed__map = make_crossed_map(threshold, i_event, layar, filename)
        hitmap_3d.append(crossed__map)
    hitmap_3d = np.array(hitmap_3d)

    SHOWING_RANGE = (-100, 100)
    X_LEN = Rhombus(0, [0, 0, 0]).x_len
    Y_LEN = Rhombus(0, [0, 0, 0]).y_len

    pixels = []
    pix_color = []
    pix_index = 0
    for i_layer in range(-4, 4):
        for i in range(-2, 2):
            for j in range(-2, 2):
                pix = Rhombus(
                    pix_index,
                    [X_LEN*(i-j), Y_LEN*(i+j), 8*i_layer]
                )
                if hitmap_3d[i_layer + 4][i + 2, j + 2] == 1.0:
                    pix_color.append('red')
                else:
                    pix_color.append('cyan')

                pixels.append(pix)
                pix_index += 1

    # set data
    data_scinti_mesh = []
    index = 0
    for pix in pixels:
        x, y, z = pix.get_vertices().T
        i, j, k = pix.get_faces().T

        data_scinti_mesh.append(
            go.Mesh3d(
                x=x, y=y, z=z, i=i, j=j, k=k,
                color=pix_color[index],
                opacity=0.05
            )
        )
        index += 1

    layout = go.Layout(
        scene=dict(
            xaxis=dict(nticks=1, range=SHOWING_RANGE,),
            yaxis=dict(nticks=1, range=SHOWING_RANGE,),
            zaxis=dict(nticks=1, range=SHOWING_RANGE,),

        )
    )

    fig = make_subplots(rows=2, cols=2, specs=[[{'type': 'mesh3d'}, {'type': 'mesh3d'}], [{'type': 'mesh3d'}, {}]])
    for i in range(len(data_scinti_mesh)):
        fig.add_trace(data_scinti_mesh[i], row=1, col=1)
        fig.add_trace(data_scinti_mesh[i], row=1, col=2)
        fig.add_trace(data_scinti_mesh[i], row=2, col=1)

    fig.update_layout(layout)
    fig.update_layout(height=900, width=1500)

    fig.update_layout(scene2_aspectmode='data')

    fig.update_layout(scene3_aspectmode='data')
    fig.update_scenes(camera=dict(
        eye=dict(x=0.7, y=0, z=0)
    ),
        xaxis_showticklabels=False,
        yaxis_showticklabels=False,
        zaxis_showticklabels=False,
        row=1, col=1)
    fig.update_scenes(camera=dict(
        eye=dict(x=0, y=3.0, z=0)
    ),
        camera_projection_type="orthographic",
        xaxis_showticklabels=False,
        yaxis_showticklabels=False,
        zaxis_showticklabels=False,
        row=2, col=1)
    fig.update_scenes(camera=dict(
        eye=dict(x=0, y=0, z=2.7)
    ),
        camera_projection_type="orthographic",
        xaxis_showticklabels=False,
        yaxis_showticklabels=False,
        zaxis_showticklabels=False,
        row=1, col=2)

    fig.update_scenes(xaxis_visible=False, yaxis_visible=False, zaxis_visible=False)
    fig.update_layout(title_text="{} event {}".format(filename, i_event))

    filename_short = filename.split('/')[-1]
    os.makedirs("img_{}".format(filename_short), exist_ok=True)
    fig.write_image("img_{}/event{}.png".format(filename_short, i_event), scale=10)
    fig.write_html("img_{}/event{}.html".format(filename_short, i_event))
    print("png and html was written to img_{}/.".format(filename))


if __name__ == "__main__":
    import sys
    threshold = int(sys.argv[1])
    i_event = int(sys.argv[2])
    filename = str(sys.argv[3])
    save_hitmap_as_html_png(threshold, i_event, filename)
