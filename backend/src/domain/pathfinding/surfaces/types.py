from dataclasses import dataclass


@dataclass
class Surface:
    center_x: float
    center_y: float


@dataclass
class RoundSurface(Surface):
    radius: float


@dataclass
class RectangleSurface(Surface):
    width: float
    height: float
