from injector import Module, Binder
from src.argparser import args
from src.domain.GeneralEventEmitter import GeneralEventEmitter
from src.domain.robot.RobotEventEmitter import RobotEventEmitter
from src.domain.sequence.SequenceEventEmitter import SequenceEventEmitter
from src.infrastructure.event_emitters.socket.GeneralSocketEventEmitter import GeneralSocketEventEmitter
from src.infrastructure.event_emitters.socket.RobotSocketEventEmitter import RobotSocketEventEmitter
from src.infrastructure.event_emitters.socket.SequenceSocketEventEmitter import SequenceSocketEventEmitter


class EventEmittersContext(Module):

    def configure(self, binder: Binder):
        if args.event_type == 'socket':
            binder.bind(GeneralEventEmitter, to=GeneralSocketEventEmitter)
            binder.bind(SequenceEventEmitter, to=SequenceSocketEventEmitter)
            binder.bind(RobotEventEmitter, to=RobotSocketEventEmitter)
