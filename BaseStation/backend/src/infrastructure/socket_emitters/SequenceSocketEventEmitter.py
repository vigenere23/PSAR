from src.domain.sequence import SequenceEventEmitter


class SequenceSocketEventEmitter(SequenceEventEmitter):

    def __init__(self, socketio):
        self.__socketio = socketio
        self.__namespace = '/sequence'

    def send_task_started(self, task_name):
        self.__socketio.emit(
            'task_started', task_name, namespace=self.__namespace
        )

    def send_sequence_ended(self):
        self.__socketio.emit('ended', namespace=self.__namespace)

    def send_error(self, task_name, message):
        self.__socketio.emit(
            'error',
            {'task': task_name, 'message': message},
            namespace=self.__namespace
        )
