from pinject import BindingSpec
from .SequenceContext import SequenceContext
from src.argparser import args


class MainContext(BindingSpec):

    def __init__(self, event_instance=None, thread_start=None, thread_sleep=None):
        super().__init__()
        self.__event_instance = event_instance
        self.__thread_start = thread_start
        self.__thread_sleep = thread_sleep

    def configure(self, bind):
        bind(args.event_type, to_instance=self.__event_instance)
        bind('thread_start', to_instance=self.__thread_start)
        bind('thread_sleep', to_instance=self.__thread_sleep)

    def dependencies(self):
        return [
            SequenceContext()
        ]
