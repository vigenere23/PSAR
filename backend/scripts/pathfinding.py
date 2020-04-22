import time
import numpy as np
from matplotlib import pyplot as plt
from pathfinding.finder.dijkstra import DijkstraFinder
from pathfinding.finder.finder import DiagonalMovement
from src.domain.pathfinding.types import Table, Robot
from src.domain.pathfinding.PathFindingGrid import PathFindingGrid
from src.domain.pathfinding.PathFinder import PathFinder
from src.domain.pathfinding.surfaces.types import RoundSurface, RectangleSurface
from src.domain.pathfinding.surfaces.SurfaceCalculatorFactory import SurfaceCalculatorFactory
from src.domain.pathfinding.helpers.WeightDecayCalculator import WeightDecayCalculator
from src.domain.coordinates.Point2D import Point2D
from src.domain.coordinates.CoordinateTransformer import CoordinateTranformer
from src.domain.coordinates.systems.TableCoordinateSystem import TableCoordinateSystem


# ALL MEASURES IN CM
TABLE_WIDTH = 231.0
TABLE_HEIGHT = 111.0
PRECISION = 1.0
SAFE_PADDING = 0.5 * PRECISION  # + 0.5 * precision padding included in algorithm
ROBOT_RADIUS = 17.5  # half of robot's width, could change in future
PILLAR_RADIUS = 12.5


table = Table(TABLE_WIDTH, TABLE_HEIGHT)
robot = Robot(width=30.0, height=30.0, max_radius=ROBOT_RADIUS)
weight_decay_calculator = WeightDecayCalculator(order=3, max_value=max(table.width, table.height))
table_coordinate_system = TableCoordinateSystem(table.width, table.height)
surface_calculator_factory = SurfaceCalculatorFactory()
coordinate_transformer = CoordinateTranformer()

obstacles = [
    RoundSurface(table.width / 3, table.height / 3, PILLAR_RADIUS),
    RoundSurface(2 * table.width / 3, 2 * table.height / 3, PILLAR_RADIUS),
    RectangleSurface(table.width / 2, 0, table.width, 0),
    RectangleSurface(table.width / 2, table.height, table.width, 0),
    RectangleSurface(0, table.height / 2, 0, table.height),
    RectangleSurface(table.width, table.height / 2, 0, table.height)
]

finder = DijkstraFinder(diagonal_movement=DiagonalMovement.always)

path_finding_grid = PathFindingGrid(table, robot, coordinate_transformer, table_coordinate_system, surface_calculator_factory)
path_finder = PathFinder(finder, coordinate_transformer, table_coordinate_system)


grid_generation_times = []
path_finding_times = []
precisions = np.linspace(0.7, 3.0, 24)
# precisions = [1.0]

for PRECISION in precisions:
    border_width = 2 * PRECISION + ROBOT_RADIUS + SAFE_PADDING
    start = Point2D(0.0 + border_width, table.height / 3)
    end = Point2D(table.width - border_width, 2 * table.height / 3)

    grid_generation_started_time = time.time()
    path_finding_grid.generate(obstacles, PRECISION, SAFE_PADDING, weight_decay_calculator)
    grid_generation_time = time.time() - grid_generation_started_time

    path_finding_started_time = time.time()
    path_found = path_finder.find_path(path_finding_grid, start.to_numpy(), end.to_numpy())
    path_finding_time = time.time() - path_finding_started_time

    grid_generation_times.append(grid_generation_time)
    path_finding_times.append(path_finding_time)

    print(path_found.grid.grid_str(path=path_found.path, start=start.to_tuple(), end=end.to_tuple()))
    print(f'{path_found.operations} operations nedded, resulting in a path of length {len(path_found.path)}')
    print(f'grid generation done in {grid_generation_time} seconds')
    print(f'path finding done in {path_finding_time} seconds')
    print(f'TOTAL done in {grid_generation_time + path_finding_time} seconds')

fig = plt.figure()
fig.suptitle('Time taken for each step in path finding')
plt.xlabel('Precision (in cm)')
plt.ylabel('Time (in s)')
plt.plot(precisions, grid_generation_times, label="Grid generation")
plt.plot(precisions, path_finding_times, label="Path finding")
plt.plot(precisions, np.array(grid_generation_times) + np.array(path_finding_times), label="Total")
plt.legend()
fig.savefig('./assets/images/test.png')
