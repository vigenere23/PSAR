import numpy as np
from unittest import TestCase
from src.domain.coordinates.Point3D import Point3D


class Point3DTest(TestCase):

    def test_coordinates_are_initialized_in_correct_order(self):
        x, y, z = (-3.1654, 12.94654, 0.265454)
        point = Point3D(x, y, z)
        self.assertEquals(point.x, x)
        self.assertEquals(point.y, y)
        self.assertEquals(point.z, z)

    def test_x_and_y_are_transformed_to_floats(self):
        point = Point3D(-1, 2, 4)
        self.assertIsInstance(point.x, float)
        self.assertIsInstance(point.y, float)
        self.assertIsInstance(point.z, float)

    def test_from_numpy_1_by_3_shape_is_permitted(self):
        shape = (1, 3)
        ndarray = np.array([1, 2, 3]).reshape(shape)

        try:
            Point3D.from_numpy(ndarray)
        except Exception:
            self.fail(f'should accept numpy shape {shape}')

    def test_from_numpy_3_by_1_shape_is_permitted(self):
        shape = (3, 1)
        ndarray = np.array([1, 2, 3]).reshape(shape)

        try:
            Point3D.from_numpy(ndarray)
        except Exception:
            self.fail(f'should accept numpy shape {shape}')

    def test_from_numpy_3_elements_shape_is_permitted(self):
        shape = (3,)
        ndarray = np.array([1, 2, 3]).reshape(shape)

        try:
            Point3D.from_numpy(ndarray)
        except Exception:
            self.fail(f'should accept numpy shape {shape}')

    def test_to_numpy_coordinates_order_is_preserved(self):
        x, y, z = (-1, 2, 4)
        point = Point3D(x, y, z)
        ndarray = point.to_numpy(shape=(3,))
        self.assertEquals(ndarray[0], x)
        self.assertEquals(ndarray[1], y)
        self.assertEquals(ndarray[2], z)

    def test_to_numpy_shape_is_applied(self):
        point = Point3D(-1, 2, 4)
        shape = (1, 3)
        ndarray = point.to_numpy(shape=shape)
        self.assertEquals(ndarray.shape, shape)
