from src.domain.robot.Robot import Robot
from src.interfaces.socket_api.RobotSocketEventHandler import RobotSocketEventHandler
from src.infrastructure.event_emitters.socket.RobotSocketEventEmitter import RobotSocketEventEmitter


class SocketHandlersContext:

    def __init__(self, socket):
        self.__socket = socket

    def register(self):
        robot_socket_event_emitter = RobotSocketEventEmitter(self.__socket)
        robot = Robot(robot_socket_event_emitter)
        robot_socket_event_handler = RobotSocketEventHandler(robot)
        self.__socket.register_namespace(robot_socket_event_handler)
