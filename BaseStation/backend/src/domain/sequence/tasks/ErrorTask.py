from . import Task

class ErrorTask(Task):
  
  def __init__(self, socketio):
    super().__init__('Error')
    self.__socketio = socketio

  def execute(self):
    raise RuntimeError("Unprocessable data from world camera")
