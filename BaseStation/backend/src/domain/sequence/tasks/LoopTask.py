from .. import Task

class LoopTask(Task):
  
    def __init__(self, socketio):
        super().__init__('Loop')
        self.__socketio = socketio

    def execute(self):
        for i in range(5):
            self.__socketio.send('This is the message #{} from within the task!'.format(i))
            self.__socketio.sleep(1)
