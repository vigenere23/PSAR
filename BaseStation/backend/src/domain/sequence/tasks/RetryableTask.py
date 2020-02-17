from .. import Task, Retryable
from ..exceptions import RetryException


class RetryableTask(Task):

    def __init__(self, socket):
        self.__socket = socket

    @Retryable(2)
    def execute(self):
        self.__socket.sleep(1)
        self.__socket.send('... doing something')
        raise RetryException(self.name())
