import numpy as np
from src.domain.pathfinding.surfaces.SurfaceCalculator import SurfaceCalculator
from src.domain.pathfinding.surfaces.SurfaceType import SurfaceType
from src.domain.pathfinding.surfaces.types import RectangleSurface


class RectangleSurfaceCalculator(SurfaceCalculator):

    def __init__(self, rectangle_surface: RectangleSurface):
        self.__rectangle_surface = rectangle_surface

    def get_points(self, x_values: np.ndarray, y_values: np.ndarray, precision: float, padding: float, surface_type: SurfaceType) -> np.ndarray:
        x, y = self.__rectangle_surface.center_x, self.__rectangle_surface.center_y
        half_width = self.__rectangle_surface.width / 2 + padding
        half_height = self.__rectangle_surface.height / 2 + padding

        x_values = x_values[np.where((x_values >= x - half_width - 0.5 * precision) & (x_values <= x + half_width + 0.5 * precision))]
        y_values = y_values[np.where((y_values >= y - half_height - 0.5 * precision) & (y_values <= y + half_height + 0.5 * precision))]
        X, Y = np.meshgrid(x_values, y_values)
        search_grid = np.array([X.flatten(), Y.flatten()]).T
        x_values = search_grid[:, 0]
        y_values = search_grid[:, 1]

        if surface_type == SurfaceType.FILL:
            return search_grid
        elif surface_type == SurfaceType.CONTOUR:
            indices = self.__rectangle_contour_indices(x_values, y_values)
            return search_grid[indices]

    def __rectangle_contour_indices(self, x_values, y_values):
        return np.where(
            (x_values == x_values[0]) | (x_values == x_values[-1]) |
            (y_values == y_values[0]) | (y_values == y_values[-1])
        )
