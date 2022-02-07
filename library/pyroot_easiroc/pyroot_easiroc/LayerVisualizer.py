from . import TrackReconstructorBase
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
from PIL import Image, ImageChops


def crop_bg(img):
    bw_img = img.convert(mode='1', dither=None)
    bw_inv_img = ImageChops.invert(bw_img)
    crop_range = bw_inv_img.convert('RGB').getbbox()
    crop_img = img.crop(crop_range)
    return crop_img


def get_concat_v(imgs):
    total_heigt = sum([img.height for img in imgs])
    dst = Image.new('RGB', (imgs[0].width, total_heigt))
    dst.paste(imgs[0], (0, 0))
    current_height = 0
    for i in range(1, len(imgs)):
        current_height += imgs[i-1].height
        dst.paste(imgs[i], (0, current_height))
    return dst


class LayerVisualizer:
    def __init__(self, tr: TrackReconstructorBase):
        self._tr = tr
        self._init_fig()
        self._draw_layers()

    def _init_fig(self):
        self._fig = make_subplots(
            rows=8, cols=1,
            specs=[
                [{'type': 'mesh3d'}] for _ in range(8)
            ]
        )
        self._fig.update_layout(height=3600*8, width=3000)
        self._fig.update_scenes(
            xaxis=dict(nticks=1, range=self._tr.SHOWING_RANGE,),
            yaxis=dict(nticks=1, range=self._tr.SHOWING_RANGE,),
            zaxis=dict(nticks=1, range=self._tr.SHOWING_RANGE,),
            xaxis_visible=False,
            yaxis_visible=False,
            zaxis_visible=False,
            camera_projection_type="orthographic",
            camera=dict(eye=dict(x=0, y=0, z=1))
        )

    def _draw_layers(self):
        self._draw_a_layer(7, 1, 1)
        self._draw_a_layer(6, 2, 1)
        self._draw_a_layer(5, 3, 1)
        self._draw_a_layer(4, 4, 1)
        self._draw_a_layer(3, 5, 1)
        self._draw_a_layer(2, 6, 1)
        self._draw_a_layer(1, 7, 1)
        self._draw_a_layer(0, 8, 1)

    def _draw_a_layer(self, i_layer, row, col):
        for i_pix in range(i_layer*16, i_layer*16 + 16):
            x, y, z = self._tr.pixels[i_pix].get_vertices().T
            i, j, k = self._tr.pixels[i_pix].get_faces().T
            self._fig.add_trace(
                go.Mesh3d(
                    x=x, y=y, z=z, i=i, j=j, k=k,
                    color=self._tr.pix_color[i_pix],
                ),
                row=row, col=col
            )

    def write_fig(self):
        os.makedirs("img_{}".format(self._tr._filename_short), exist_ok=True)
        self._save_file_name = "img_{}/layer_{}.png".format(self._tr._filename_short, self._tr._i_event)
        self._fig.write_image("tmp.png")
        self._crop_image()

    def _crop_image(self):
        input_image = Image.open("tmp.png")
        cropped_images = []
        for i in range(0, 8):
            cropped_image = input_image.crop((
                0,
                int(input_image.height * (i/8)),
                input_image.width,
                int(input_image.height * ((i+1)/8))
            ))
            cropped_images.append(crop_bg(cropped_image))
        cropped_concatted_image = get_concat_v(cropped_images)
        cropped_concatted_image.save(self._save_file_name)
        print("{} saved".format(self._save_file_name))
