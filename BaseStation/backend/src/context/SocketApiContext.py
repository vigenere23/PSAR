from injector import Injector
from src.interfaces.socket_api.SequenceSocketEventHandler import SequenceSocketEventHandler


class SocketApiContext:

    def __init__(self, injector: Injector, register_fn):
        self.injector = injector
        self.register_fn = register_fn

    def register_routes(self):
        sequence_event_handler = self.injector.get(SequenceSocketEventHandler)
        self.register_fn(sequence_event_handler)
