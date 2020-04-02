from src.domain.pathfinding.surfaces.types import Surface, RoundSurface, RectangleSurface
from src.domain.pathfinding.surfaces.SurfaceCalculator import SurfaceCalculator
from src.domain.pathfinding.surfaces.RoundSurfaceCalculator import RoundSurfaceCalculator
from src.domain.pathfinding.surfaces.RectangleSurfaceCalculator import RectangleSurfaceCalculator


class SurfaceCalculatorFactory:

    def create_for_surface(self, surface: Surface) -> SurfaceCalculator:
        if isinstance(surface, RoundSurface):
            return RoundSurfaceCalculator(surface)
        elif isinstance(surface, RectangleSurface):
            return RectangleSurfaceCalculator(surface)
        else:
            raise ValueError(f'no surface calculator for surface {surface.__class__.__name__}')
