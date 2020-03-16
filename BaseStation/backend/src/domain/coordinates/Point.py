import numpy as np
from abc import ABC, abstractmethod


class Point(ABC):

    @classmethod
    @abstractmethod
    def from_numpy(cls, ndarray: np.array):
        pass

    @abstractmethod
    def to_numpy(self):
        pass
