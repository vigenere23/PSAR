from .. import Task

class EndOfSequenceTask(Task):

    def __init__(self, socketio):
        super().__init__(name='End of sequence')
        self.__socketio = socketio

    def execute(self):
        self.__socketio.emit('ended', namespace='/sequence')
