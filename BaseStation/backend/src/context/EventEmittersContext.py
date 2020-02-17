from pinject import BindingSpec
from src.infrastructure.event_emitters.socket import SequenceSocketEventEmitter


class EventEmittersContext(BindingSpec):

    def __init__(self, event_type, event_instance, thread_starter):
        self.__event_type = event_type
        self.__event_instance = event_instance
        self.__thread_starter = thread_starter

    def configure(self, bind):
        bind(self.__event_type, to_instance=self.__event_instance)
        bind('thread_starter', to_instance=self.__thread_starter)

        if self.__event_type == 'socket':
            bind('sequence_event_emitter', to_class=SequenceSocketEventEmitter)
