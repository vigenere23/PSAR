import unittest
from .SocketApiTest import SocketApiTest
from src.app import app, socketio

class TestNamespaceTest(SocketApiTest):

    def test_connection(self):
        self.assertTrue(self.app.is_connected())

if __name__ == '__main__':
    unittest.main()
