from injector import Module, Binder
from src.argparser import args
from src.domain.ThreadManager import ThreadManager
from src.infrastructure.thread_managers.SocketThreadManager import SocketThreadManager


class ThreadManagerContext(Module):

    def configure(self, binder: Binder):
        if args.event_type == 'socket':
            binder.bind(ThreadManager, to=SocketThreadManager)
