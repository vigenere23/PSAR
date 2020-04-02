import numpy as np
from src.domain.coordinates.CoordinateSystem import CoordinateSystem


class CoordinateTranformer:

    def transform(self, points: np.ndarray, input: CoordinateSystem, output: CoordinateSystem) -> np.ndarray:
        points_copy = np.copy(points)
        points_copy[:, 0] *= output.reference_width / input.reference_width
        points_copy[:, 1] *= output.reference_height / input.reference_height
        return output.transform(points_copy)
