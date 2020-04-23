import unittest
from unittest.mock import Mock


class MockTestCase(unittest.TestCase):

    def assertCalled(self, mock_method, times=None):
        if not isinstance(mock_method, Mock):
            raise ValueError(
                "'mock_method' should be of type 'unittest.Mock', not '{}'"
                .format(mock_method.__class__.__name__)
            )
        if times is None:
            self.assertGreaterEqual(mock_method.call_count, 1)
        else:
            self.assertEqual(mock_method.call_count, times)

    def assertNotCalled(self, mock_method):
        self.assertCalled(mock_method, times=0)

    def assertCalledOnce(self, mock_method):
        self.assertCalled(mock_method, times=1)
