import unittest
from src.app import app, socketio


class SocketApiTest(unittest.TestCase):

    def setUp(self):
        app.testing = True
        flask_test_client = app.test_client()
        self.app = socketio.test_client(
            app, flask_test_client=flask_test_client
        )
