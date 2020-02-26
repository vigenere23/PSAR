from .. import Task, Retryable


class RetryableTask(Task):

    def __init__(self, socket, thread_sleep):
        self.__socket = socket
        self.__thread_sleep = thread_sleep

    @Retryable(5)
    def execute(self):
        self.__thread_sleep(1)
        self.__socket.send('... doing something')
        self.retry()
