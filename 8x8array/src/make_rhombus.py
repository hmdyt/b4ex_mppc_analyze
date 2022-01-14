from typing import List, Tuple
import numpy as np
import itertools
import numpy as np

class Rhombus:
    #原点は菱形の立体の中心
    # l:  シンチレータの横幅[cm]
    l = 4
    theta = np.radians(7)
    # x_len, y_len xが短いほうの対角線
    x_len = l * np.sin(theta) / np.sin(2*theta)
    y_len = l * np.cos(theta) / np.sin(2*theta)
    #シンチレータのz
    z_len = 2

    def __init__(self, index: int, origin_point: Tuple[float, float, float]) -> None:
        self._origin_point = np.array(origin_point)
        self._index = index
        self.create_polygon()

    def create_polygon(self) -> None:
        self._vertices = np.array([
            self._origin_point + [0, self.y_len, self.z_len],
            self._origin_point + [self.x_len, 0, self.z_len],
            self._origin_point + [0, -self.y_len, self.z_len],
            self._origin_point + [-self.x_len, 0, self.z_len],
            self._origin_point + [0, self.y_len, -self.z_len],
            self._origin_point + [self.x_len, 0, -self.z_len],
            self._origin_point + [0, -self.y_len, -self.z_len],
            self._origin_point + [-self.x_len, 0, -self.z_len]
        ])

        #三角形の組み合わせ
        self._faces = np.array(
            [v for v in itertools.combinations([0, 1, 2, 3], 3)] + 
            [v for v in itertools.combinations([4, 5, 6, 7], 3)] + 
            [v for v in itertools.combinations([0, 1, 4, 5], 3)] + 
            [v for v in itertools.combinations([1, 2, 5, 6], 3)] + 
            [v for v in itertools.combinations([2, 3, 6, 7], 3)] + 
            [v for v in itertools.combinations([3, 0, 7, 4], 3)]
        )
    
    def get_index(self) -> int:
        return self._index

    
    def get_vertices(self):
        return self._vertices
    
    def get_faces(self):
        return self._faces