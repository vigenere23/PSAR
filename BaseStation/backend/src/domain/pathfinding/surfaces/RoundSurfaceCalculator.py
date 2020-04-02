import numpy as np
from src.domain.pathfinding.surfaces.SurfaceCalculator import SurfaceCalculator
from src.domain.pathfinding.surfaces.SurfaceType import SurfaceType
from src.domain.pathfinding.surfaces.types import RoundSurface


class RoundSurfaceCalculator(SurfaceCalculator):

    def __init__(self, round_surface: RoundSurface):
        self.__round_surface = round_surface

    def get_points(self, x_values: np.ndarray, y_values: np.ndarray, precision: float, padding: float, surface_type: SurfaceType) -> np.ndarray:
        x, y = self.__round_surface.center_x, self.__round_surface.center_y
        radius = self.__round_surface.radius + padding

        x_values = x_values[np.where((x_values >= x - radius - 0.5 * precision) & (x_values <= x + radius + 0.5 * precision))]
        y_values = y_values[np.where((y_values >= y - radius - 0.5 * precision) & (y_values <= y + radius + 0.5 * precision))]
        X, Y = np.meshgrid(x_values, y_values)
        search_grid = np.array([X.flatten(), Y.flatten()]).T
        x_values = search_grid[:, 0]
        y_values = search_grid[:, 1]

        if surface_type == SurfaceType.FILL:
            indices = self.__inside_circle_indices(x_values, y_values, x, y, radius, precision)
        elif surface_type == SurfaceType.CONTOUR:
            indices = self.__circle_contour_indices(x_values, y_values, x, y, radius, precision)

        return search_grid[indices]

    def __inside_circle_indices(self, x_values: float, y_values: float, x: float, y: float, radius: float, precision: float):
        return np.where(np.square(x_values - x) + np.square(y_values - y) <= np.square(radius + 0.5 * precision))

    def __circle_contour_indices(self, x_values: float, y_values: float, x: float, y: float, radius: float, precision: float):
        return np.where(
            (np.square(x_values - x) + np.square(y_values - y) >= np.square(radius - 0.5 * precision)) &
            (np.square(x_values - x) + np.square(y_values - y) <= np.square(radius + 0.5 * precision))
        )
