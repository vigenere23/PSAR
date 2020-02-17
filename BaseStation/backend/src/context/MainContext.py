from pinject import BindingSpec
from .EventEmittersContext import EventEmittersContext


class MainContext(BindingSpec):

    def __init__(self, event_type=None, event_instance=None):
        super().__init__()
        self.__event_type = event_type
        self.__event_instance = event_instance

    def dependencies(self):
        return [
            EventEmittersContext(self.__event_type, self.__event_instance)
        ]
