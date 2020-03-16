import numpy as np
from src.domain.coordinates.Point import Point


class Point3D(Point):

    __DEFAULT_SHAPE = (1, 3)
    __ACCEPTED_SHAPES = [
        (1, 3),
        (3, 1),
        (3,)
    ]

    def __init__(self, x: float, y: float, z: float):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    @classmethod
    def from_numpy(cls, ndarray: np.ndarray):
        if (ndarray.shape not in cls.__ACCEPTED_SHAPES):
            raise ValueError(f'shape {ndarray.shape} not accepted for Point2D')

        x, y, z = ndarray.reshape((3,))

        return Point3D(x, y, z)

    def to_numpy(self, shape=__DEFAULT_SHAPE):
        return np.array([self.x, self.y, self.z]).reshape(shape)

    def __repr__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def __str__(self):
        return self.__repr__()
