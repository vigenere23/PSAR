import numpy as np
from abc import ABC, abstractmethod


class CoordinateSystem(ABC):

    def __init__(self, reference_width, reference_height):
        self.reference_width = reference_width
        self.reference_height = reference_height

    @abstractmethod
    def transform(self, a: np.ndarray):
        pass
