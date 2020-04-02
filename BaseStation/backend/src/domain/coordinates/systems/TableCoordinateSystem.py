import numpy as np
from src.domain.coordinates.CoordinateSystem import CoordinateSystem


class TableCoordinateSystem(CoordinateSystem):

    def transform(self, a: np.ndarray):
        return a
