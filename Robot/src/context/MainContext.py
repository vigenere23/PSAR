from injector import Module, Binder
from socketio.client import Client
from src.context.SerialPortContext import SerialPortContext


class MainContext(Module):

    def __init__(self, event_instance=None):
        super().__init__()
        self.__event_instance = event_instance

    def configure(self, binder: Binder):
        binder.bind(Client, to=self.__event_instance)
        binder.install(SerialPortContext())
