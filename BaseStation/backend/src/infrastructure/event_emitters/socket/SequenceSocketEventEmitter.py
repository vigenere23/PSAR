from src.domain.sequence import SequenceEventEmitter


class SequenceSocketEventEmitter(SequenceEventEmitter):

    def __init__(self, socket):
        self.__socket = socket
        self.__namespace = '/sequence'

    def send_task_started(self, task_name):
        self.__socket.emit(
            'task_started', task_name, namespace=self.__namespace
        )

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
