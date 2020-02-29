from injector import inject
from flask_socketio import SocketIO
from src.domain.ThreadManager import ThreadManager


class SocketThreadManager(ThreadManager):

    @inject
    def __init__(self, socket: SocketIO):
        self.__socket = socket

    def sleep(self, seconds):
        return self.__socket.sleep(seconds)

    def start(self, *args, **kwargs):
        return self.__socket.start_background_task(*args, **kwargs)
