from dataclasses import dataclass
from pathfinding.core.grid import Grid


@dataclass
class PathFound:
    path: list
    operations: int
    grid: Grid


@dataclass
class Table:
    width: float
    height: float


@dataclass
class Robot:
    width: float
    height: float
    max_radius: float
