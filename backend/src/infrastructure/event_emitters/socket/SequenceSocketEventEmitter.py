from injector import inject
from flask_socketio import SocketIO
from src.domain.sequence.SequenceEventEmitter import SequenceEventEmitter


class SequenceSocketEventEmitter(SequenceEventEmitter):

    @inject
    def __init__(self, socket: SocketIO):
        self.__socket = socket
        self.__namespace = '/sequence'

    def send_task_started(self, task_name):
        self.__socket.emit(
            'task_started', task_name, namespace=self.__namespace
        )

    def send_task_ended(self, task_name):
        self.__socket.emit(
            'task_ended', task_name, namespace=self.__namespace
        )

    def send_sequence_started(self, task_names: list):
        self.__socket.emit('started', {'tasks': task_names}, namespace=self.__namespace)

    def send_sequence_ended(self):
        self.__socket.emit('ended', namespace=self.__namespace)

    def send_task_warning(self, task_name, message):
        self.__socket.emit(
            'task_warning',
            {'task': task_name, 'message': message},
            namespace=self.__namespace
        )

    def send_task_error(self, task_name, message):
        self.__socket.emit(
            'task_error',
            {'task': task_name, 'message': message},
            namespace=self.__namespace
        )
