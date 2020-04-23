from flask_socketio import SocketIO
from injector import inject
from src.domain.GeneralEventEmitter import GeneralEventEmitter


class GeneralSocketEventEmitter(GeneralEventEmitter):

    @inject
    def __init__(self, socket: SocketIO):
        self.__socket = socket

    def send_message(self, message):
        self.__socket.emit('message', message)
