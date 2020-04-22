import numpy as np
from src.domain.coordinates.CoordinateSystem import CoordinateSystem


class GridCoordinateSystem(CoordinateSystem):

    def transform(self, a: np.ndarray):
        return np.around(a).astype(int)
