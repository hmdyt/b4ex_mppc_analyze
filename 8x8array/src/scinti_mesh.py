from types import ClassMethodDescriptorType
from numpy.core.defchararray import _unary_op_dispatcher
import plotly.graph_objects as go
import numpy as np
from make_rhombus import Rhombus
import make_hitmap_3D
from plotly.subplots import make_subplots


SHOWING_RANGE = (-100, 100)
X_LEN = Rhombus(0, [0, 0, 0]).x_len
Y_LEN = Rhombus(0, [0, 0, 0]).y_len

## prepare pixels
pixels = []

#main(thereshold, i_event)
hitmap_3D = make_hitmap_3D.main()
pixels_rhombus = []
pix_index_rhombus = []

pix_color = []
pix_index = 0
for i_layer in range(-4, 4):
    for i in range(-2, 2):
        for j in range(-2, 2):
            pix = Rhombus(
                pix_index,
                [X_LEN*(i-j), Y_LEN*(i+j), 8*i_layer]
                )
            if hitmap_3D[i_layer + 4][i + 2, j + 2] == 1.0:
                pix_rhombus = pix
                pixels_rhombus.append(pix_rhombus)
                pix_index_rhombus.append(pix_index)
                pix_color.append('red')
            else:
                pix_color.append('cyan')

            pixels.append(pix)
            pix_index += 1

## set data
data_scinti_mesh = []
index = 0
for pix in pixels:
    x, y, z = pix.get_vertices().T
    i, j, k = pix.get_faces().T

    data_scinti_mesh.append(
        go.Mesh3d(
            x=x, y=y, z=z, i=i, j=j, k=k,
            color = pix_color[index],
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

fig = make_subplots(rows=2, cols=2, specs=[[{'type': 'mesh3d'},{'type': 'mesh3d'}],[{'type': 'mesh3d'},{}]])
for i in range(len(data_scinti_mesh)):
    fig.add_trace(data_scinti_mesh[i], row = 1, col = 1)
    fig.add_trace(data_scinti_mesh[i], row = 1,col=2)
    fig.add_trace(data_scinti_mesh[i], row=2, col=1)

fig.update_layout(layout)
fig.update_layout(height=900, width=1500)
fig.update_layout(scene2_aspectmode = 'data')

fig.update_layout(scene3_aspectmode='data')
fig.update_scenes(camera = dict(
            eye = dict(x = 0.7, y = 0, z = 0)
        ),
        row=1, col=1)
fig.update_scenes(camera = dict(
            eye = dict(x = 0, y = 3.0, z = 0)
        ),
        row=2, col=1)
fig.update_scenes(camera = dict(
            eye = dict(x = 0, y = 0, z = 2.7)
        ),
        row=1, col=2)

fig.show()
fig.write_image("test01.jpeg")
#take pictures toword x,y,z each i event
#selecy data