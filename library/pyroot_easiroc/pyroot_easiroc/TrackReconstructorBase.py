from typing import List
import numpy as np
import ROOT as r
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from .Rhombus import Rhombus
from .HitArrayGen import HitArrayGen
r.gROOT.SetBatch()


class TrackReconstructorBase:
    SHOWING_RANGE = (-100, 100)
    X_LEN = Rhombus(0, [0, 0, 0]).x_len
    Y_LEN = Rhombus(0, [0, 0, 0]).y_len

    def __init__(self, rootfile_path: str, threshold_s: List[int]) -> None:
        if len(threshold_s) != 64:
            print("invalid threshold list length")
            exit()
        self._rootfile_path = rootfile_path
        self._hit_array_gen = HitArrayGen(self._rootfile_path)
        for ch in range(64):
            self._hit_array_gen.set_threshold(ch, threshold_s[ch])
        self._hit_array_gen.generate_hit_array()
        self._hit_array = self._hit_array_gen.get_hit_array()
        self._make_point()
        self._init_fig()

    def _make_point(self):
        self._point = np.zeros(shape=[8, 4, 4, 3], dtype=np.float)
        for i_layer in range(-4, 4):
            for i in range(-2, 2):
                for j in range(-2, 2):
                    origin_point = [self.X_LEN * (i - j), self.Y_LEN * (i + j), 8 * i_layer]
                    self._point[i_layer + 4][i + 2][j + 2] = np.array(origin_point, dtype=np.float)

    def get_point(self, i_layer, i, j):
        return self._point[i_layer][i][j]

    def _init_fig(self):
        self._fig = make_subplots(
            rows=2, cols=2,
            specs=[
                [{'type': 'mesh3d'}, {'type': 'mesh3d'}],
                [{'type': 'mesh3d'}, {}]
            ]
        )
        layout = go.Layout(
            scene=dict(
                xaxis=dict(nticks=1, range=self.SHOWING_RANGE,),
                yaxis=dict(nticks=1, range=self.SHOWING_RANGE,),
                zaxis=dict(nticks=1, range=self.SHOWING_RANGE,),
            )
        )
        self._fig.update_layout(layout)
        self._fig.update_layout(height=900, width=1500)
        self._fig.update_layout(scene2_aspectmode='data')
        self._fig.update_layout(scene3_aspectmode='data')
        self._fig.update_scenes(camera=dict(
            eye=dict(x=0.7, y=0, z=0)
        ),
            xaxis_showticklabels=False,
            yaxis_showticklabels=False,
            zaxis_showticklabels=False,
            row=1, col=1)
        self._fig.update_scenes(camera=dict(
            eye=dict(x=0, y=3.0, z=0)
        ),
            camera_projection_type="orthographic",
            xaxis_showticklabels=False,
            yaxis_showticklabels=False,
            zaxis_showticklabels=False,
            row=2, col=1)
        self._fig.update_scenes(
            camera=dict(
                eye=dict(x=0, y=0, z=2.7)
            ),
            camera_projection_type="orthographic",
            xaxis_showticklabels=False,
            yaxis_showticklabels=False,
            zaxis_showticklabels=False,
            row=1, col=2
        )
        self._fig.update_scenes(xaxis_visible=False, yaxis_visible=False, zaxis_visible=False)

    def draw_mesh(self, i_event):
        self._prepare_pixel_attributes(i_event)
        self.data_scinti_mesh = []
        for i_pixels, pix in enumerate(self.pixels):
            x, y, z = pix.get_vertices().T
            i, j, k = pix.get_faces().T
            self.data_scinti_mesh.append(
                go.Mesh3d(
                    x=x, y=y, z=z, i=i, j=j, k=k,
                    color=self.pix_color[i_pixels],
                    opacity=0.05 if self.pix_color[i_pixels] == "cyan" else 1
                )
            )
        for i in range(len(self.data_scinti_mesh)):
            self._fig.add_trace(self.data_scinti_mesh[i], row=1, col=1)
            self._fig.add_trace(self.data_scinti_mesh[i], row=1, col=2)
            self._fig.add_trace(self.data_scinti_mesh[i], row=2, col=1)
        self._fig.update_layout(title_text="{} event {}".format(self._rootfile_path, i_event))

    def write_fig(self, i_event):
        filename_short = self._rootfile_path.split('/')[-1]
        os.makedirs("img_{}".format(filename_short), exist_ok=True)
        self._fig.write_image("img_{}/event{}.png".format(filename_short, i_event), scale=10)
        print("img_{}/event{}.png".format(filename_short, i_event))
        self._fig.write_html("img_{}/event{}.html".format(filename_short, i_event))
        print("img_{}/event{}.html".format(filename_short, i_event))

    def _prepare_pixel_attributes(self, i_event):
        self._i_event = i_event
        self.pixels = []
        self.pix_color = []
        self.pix_index = 0
        for i_layer in range(-4, 4):
            for i in range(-2, 2):
                for j in range(-2, 2):
                    pix = Rhombus(
                        self.pix_index,
                        [self.X_LEN * (i - j), self.Y_LEN * (i + j), 8 * i_layer]
                    )
                    if self._hit_array[i_event][i_layer + 4][i + 2, j + 2] == 1.0:
                        self.pix_color.append("black")
                    else:
                        self.pix_color.append("cyan")
                    self.pixels.append(pix)
                    self.pix_index += 1

    def show(self, i_event):
        self._init_fig()
        self.draw_mesh(i_event)
        self.write_fig(i_event)
