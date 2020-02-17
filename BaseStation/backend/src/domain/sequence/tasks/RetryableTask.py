from .. import Task, Retryable
from ..exceptions import RetryException


class RetryableTask(Task):

    def __init__(self, socketio):
        self.__socketio = socketio

    @Retryable(2)
    def execute(self):
        self.__socketio.sleep(1)
        self.__socketio.send('... doing something')
        raise RetryException(self.name())
