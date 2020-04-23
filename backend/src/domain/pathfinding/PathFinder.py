import numpy as np
from pathfinding.core.grid import Grid
from pathfinding.finder.finder import Finder
from src.domain.pathfinding.PathFindingGrid import PathFindingGrid
from src.domain.pathfinding.types import PathFound
from src.domain.coordinates.systems.GridCoordinateSystem import GridCoordinateSystem
from src.domain.coordinates.systems.TableCoordinateSystem import TableCoordinateSystem
from src.domain.coordinates.CoordinateTransformer import CoordinateTranformer


class PathFinder:

    def __init__(self, finder: Finder, coordinate_transformer: CoordinateTranformer, table_coordinate_system: TableCoordinateSystem):
        self.__finder = finder
        self.__coordinate_transformer = coordinate_transformer
        self.__table_coordinate_system = table_coordinate_system

    def find_path(self, grid: PathFindingGrid, start: np.ndarray, end: np.ndarray) -> PathFound:
        grid = Grid(matrix=grid.get_matrix())
        grid_coordinate_system = GridCoordinateSystem(grid.width - 1, grid.height - 1)

        grid_start = self.__coordinate_transformer.transform(start, self.__table_coordinate_system, grid_coordinate_system)
        grid_end = self.__coordinate_transformer.transform(end, self.__table_coordinate_system, grid_coordinate_system)

        path, operations = self.__finder.find_path(grid.node(*grid_start[0]), grid.node(*grid_end[0]), grid)

        return PathFound(path=path, operations=operations, grid=grid)
