from .. import Context
from src.interfaces.socket_handlers import RobotSocketEventHandler
from src.domain.robot.Robot import Robot
from src.infrastructure.socket_emitters import RobotSocketEventEmitter


class SocketHandlersContext(Context):

    def __init__(self, socket):
        self.__socket = socket

    def register(self):
        robot_socket_event_emitter = RobotSocketEventEmitter(self.__socket)
        robot = Robot(robot_socket_event_emitter)
        robot_socket_event_handler = RobotSocketEventHandler(robot)
        self.__socket.register_namespace(robot_socket_event_handler)
