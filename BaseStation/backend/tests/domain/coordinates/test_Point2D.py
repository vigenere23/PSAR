import numpy as np
from unittest import TestCase
from src.domain.coordinates.Point2D import Point2D


class Point2DTest(TestCase):

    def test_coordinates_are_initialized_in_correct_order(self):
        x, y = (-3.1654, 12.94654)
        point = Point2D(x, y)
        self.assertEquals(point.x, x)
        self.assertEquals(point.y, y)

    def test_x_and_y_are_transformed_to_floats(self):
        point = Point2D(-1, 2)
        self.assertIsInstance(point.x, float)
        self.assertIsInstance(point.y, float)

    def test_from_numpy_1_by_2_shape_is_permitted(self):
        shape = (1, 2)
        ndarray = np.array([1, 2]).reshape(shape)

        try:
            Point2D.from_numpy(ndarray)
        except Exception:
            self.fail(f'should accept numpy shape {shape}')

    def test_from_numpy_2_by_1_shape_is_permitted(self):
        shape = (2, 1)
        ndarray = np.array([1, 2]).reshape(shape)

        try:
            Point2D.from_numpy(ndarray)
        except Exception:
            self.fail(f'should accept numpy shape {shape}')

    def test_from_numpy_2_elements_shape_is_permitted(self):
        shape = (2,)
        ndarray = np.array([1, 2]).reshape(shape)

        try:
            Point2D.from_numpy(ndarray)
        except Exception:
            self.fail(f'should accept numpy shape {shape}')

    def test_to_numpy_coordinates_order_is_preserved(self):
        x, y = (-1, 2)
        point = Point2D(x, y)
        ndarray = point.to_numpy(shape=(2,))
        self.assertEquals(ndarray[0], x)
        self.assertEquals(ndarray[1], y)

    def test_to_numpy_shape_is_applied(self):
        point = Point2D(-1, 2)
        shape = (1, 2)
        ndarray = point.to_numpy(shape=shape)
        self.assertEquals(ndarray.shape, shape)
