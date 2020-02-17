from src.interfaces.socket import SequenceSocketEventHandler


class EventHandlersRegisterer:

    def __init__(self, object_graph, register_fn):
        self.object_graph = object_graph
        self.register_fn = register_fn

    def register_routes(self):
        sequence_event_handler = self.object_graph.provide(SequenceSocketEventHandler)
        self.register_fn(sequence_event_handler)
