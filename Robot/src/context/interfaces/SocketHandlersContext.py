from .. import Context
from src.interfaces.socket_handlers import RobotSocketEventHandler


class SocketHandlersContext(Context):

    def __init__(self, socketio):
        self.__socketio = socketio

    def register(self):
        robot_socket_event_emitter = RobotSocketEventHandler()
        self.__socketio.register_namespace(robot_socket_event_emitter)
