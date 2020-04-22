import numpy as np
from typing import List
from src.domain.pathfinding.types import Table, Robot
from src.domain.pathfinding.surfaces.types import Surface
from src.domain.pathfinding.surfaces.SurfaceType import SurfaceType
from src.domain.pathfinding.surfaces.SurfaceCalculatorFactory import SurfaceCalculatorFactory
from src.domain.coordinates.systems.TableCoordinateSystem import TableCoordinateSystem
from src.domain.coordinates.systems.GridCoordinateSystem import GridCoordinateSystem
from src.domain.coordinates.CoordinateTransformer import CoordinateTranformer
from src.domain.pathfinding.helpers.WeightDecayCalculator import WeightDecayCalculator


class PathFindingGrid:

    def __init__(self, table: Table, robot: Robot, coordinate_transformer: CoordinateTranformer, table_coordinate_system: TableCoordinateSystem, surface_calculator_factory: SurfaceCalculatorFactory):
        self.__table = table
        self.__robot = robot
        self.__coordinate_transformer = coordinate_transformer
        self.__surface_calculator_factory = surface_calculator_factory
        self.__table_coordinate_system = table_coordinate_system

    def get_matrix(self) -> np.ndarray:
        return self.__matrix

    def generate(self, obstacles: List[Surface], precision: float, safe_padding: float, weight_decay_calculator: WeightDecayCalculator):
        total_padding = self.__robot.max_radius + safe_padding
        grid_width = int(self.__table.width / precision) + 1
        grid_height = int(self.__table.height / precision) + 1

        self.__grid_coordinate_system = GridCoordinateSystem(grid_width - 1, grid_height - 1)
        self.__x_values = np.linspace(0, self.__table.width, grid_width)
        self.__y_values = np.linspace(0, self.__table.height, grid_height)
        self.__matrix = np.ones((grid_height, grid_width), dtype=np.int)

        self.__add_obstacles(obstacles, precision, total_padding)
        self.__add_force_field(obstacles, precision, total_padding, weight_decay_calculator)

    def __add_obstacles(self, obstacles: List[Surface], precision: float, padding: float):
        for obstacle in obstacles:
            surface_calculator = self.__surface_calculator_factory.create_for_surface(obstacle)
            points = surface_calculator.get_points(self.__x_values, self.__y_values, precision, padding, SurfaceType.FILL)
            points = self.__coordinate_transformer.transform(points, self.__table_coordinate_system, self.__grid_coordinate_system)
            self.__matrix[points[:, 1], points[:, 0]] = 0

    def __add_force_field(self, obstacles: List[Surface], precision: float, padding: float, weight_decay_calculator: WeightDecayCalculator):
        force_field_max_radius = max(self.__table.width, self.__table.height)

        for force_field_radius in range(1, int(force_field_max_radius) + 1):
            has_changed = False
            weight = weight_decay_calculator.get_weight(force_field_radius)

            for obstacle in obstacles:
                surface_calculator = self.__surface_calculator_factory.create_for_surface(obstacle)
                points = surface_calculator.get_points(self.__x_values, self.__y_values, precision, padding + force_field_radius * precision, SurfaceType.CONTOUR)
                points = self.__coordinate_transformer.transform(points, self.__table_coordinate_system, self.__grid_coordinate_system)

                for point in points:
                    if self.__matrix[point[1], point[0]] == 1:
                        self.__matrix[point[1], point[0]] = weight
                        has_changed = True

            if not has_changed:
                break
