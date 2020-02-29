from injector import Module, Binder
from flask_socketio import SocketIO
from src.argparser import args


class EventInstanceContext(Module):

    def __init__(self, event_instance):
        self.__event_instance = event_instance

    def configure(self, binder: Binder):
        if args.event_type == 'socket':
            binder.bind(SocketIO, to=self.__event_instance)
