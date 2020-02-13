from .. import Task, Retryable


class RetryableTask(Task):

    def __init__(self, socketio):
        super().__init__('Retryable')
        self.__socketio = socketio

    @Retryable(2)
    def execute(self):
        self.__socketio.sleep(1)
        self.__socketio.send('... doing something')
        raise RuntimeError()
