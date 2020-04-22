from injector import Injector
from src.interfaces.socket_api.RobotSocketEventHandler import RobotSocketEventHandler


class SocketApiContext:

    def __init__(self, injector: Injector, register_fn):
        self.__injector = injector
        self.__register_fn = register_fn

    def register_routes(self):
        robot_socket_event_handler = self.__injector.get(RobotSocketEventHandler)

        self.__register_fn(robot_socket_event_handler)
