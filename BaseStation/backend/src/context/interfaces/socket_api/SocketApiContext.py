from src.context import Context
from src.interfaces.socket_api import TestNamespace

class SocketApiContext(Context):

  def __init__(self, socketio):
    self.__socketio = socketio

  def register(self):
    self.__socketio.on_namespace(TestNamespace(''))
