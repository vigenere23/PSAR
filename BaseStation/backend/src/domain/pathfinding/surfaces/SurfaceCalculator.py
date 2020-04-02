import numpy as np
from abc import ABC, abstractmethod
from src.domain.pathfinding.surfaces.SurfaceType import SurfaceType


class SurfaceCalculator(ABC):

    @abstractmethod
    def get_points(self, x_values: np.ndarray, y_values: np.ndarray, precision: float, padding: float, surface_type: SurfaceType) -> np.ndarray:
        pass
