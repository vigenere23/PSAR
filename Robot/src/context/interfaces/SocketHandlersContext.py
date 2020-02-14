from .. import Context
from src.interfaces.socket_handlers import RobotSocketEventHandler


class SocketHandlersContext(Context):

    def __init__(self, socket):
        self.__socket = socket

    def register(self):
        robot_socket_event_emitter = RobotSocketEventHandler()
        self.__socket.register_namespace(robot_socket_event_emitter)
