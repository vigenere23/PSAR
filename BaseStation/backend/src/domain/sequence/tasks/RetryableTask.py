from .. import Task, Retryable
from ..exceptions import RetryException


class RetryableTask(Task):

    def __init__(self, socket, thread_sleep):
        self.__socket = socket
        self.__thread_sleep = thread_sleep

    @Retryable(2)
    def execute(self):
        self.__thread_sleep(1)
        self.__socket.send('... doing something')
        raise RetryException(self.name())
