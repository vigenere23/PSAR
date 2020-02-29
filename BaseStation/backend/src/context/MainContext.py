from injector import Module, Binder
from src.context.ThreadManagerContext import ThreadManagerContext
from src.context.SequenceContext import SequenceContext
from src.context.EventEmittersContext import EventEmittersContext
from src.context.EventInstanceContext import EventInstanceContext


class MainContext(Module):

    def __init__(self, event_instance=None):
        super().__init__()
        self.__event_instance = event_instance

    def configure(self, binder: Binder):
        binder.install(EventInstanceContext(self.__event_instance))
        binder.install(ThreadManagerContext())
        binder.install(EventEmittersContext())
        binder.install(SequenceContext())
