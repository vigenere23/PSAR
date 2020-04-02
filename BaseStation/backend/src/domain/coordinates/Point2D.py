import numpy as np
from src.domain.coordinates.Point import Point


class Point2D(Point):

    __DEFAULT_SHAPE = (1, 2)
    __ACCEPTED_SHAPES = [
        (1, 2),
        (2, 1),
        (2,)
    ]

    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    @classmethod
    def from_numpy(cls, ndarray: np.ndarray):
        if (ndarray.shape not in cls.__ACCEPTED_SHAPES):
            raise ValueError(f'shape {ndarray.shape} not accepted for Point2D')

        x, y = ndarray.reshape((2,))

        return Point2D(x, y)

    def to_numpy(self, shape=__DEFAULT_SHAPE):
        return np.array([self.x, self.y]).reshape(shape)

    def to_tuple(self) -> tuple:
        return (self.x, self.y)

    def __repr__(self):
        return str(self.to_tuple())

    def __str__(self):
        return self.__repr__()
