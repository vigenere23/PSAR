from injector import Module, Binder
from src.domain.robot.RobotEventEmitter import RobotEventEmitter
from src.infrastructure.event_emitters.socket.RobotSocketEventEmitter import RobotSocketEventEmitter


class EventEmittersContext(Module):

    def configure(self, binder: Binder):
        binder.bind(RobotEventEmitter, to=RobotSocketEventEmitter)
