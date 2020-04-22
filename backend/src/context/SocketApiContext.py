from injector import Injector
from src.interfaces.socket_api.SequenceSocketEventHandler import SequenceSocketEventHandler
from src.interfaces.socket_api.RobotSocketEventHandler import RobotSocketEventHandler
from src.interfaces.socket_api.DebugRobotSocketEventHandler import DebugRobotSocketEventHandler


class SocketApiContext:

    def __init__(self, injector: Injector, register_fn):
        self.injector = injector
        self.register_fn = register_fn

    def register_routes(self):
        sequence_event_handler = self.injector.get(SequenceSocketEventHandler)
        robot_event_handler = self.injector.get(RobotSocketEventHandler)
        debug_robot_event_handler = self.injector.get(DebugRobotSocketEventHandler)

        self.register_fn(sequence_event_handler)
        self.register_fn(robot_event_handler)
        self.register_fn(debug_robot_event_handler)
