class TaskContainer:

  def __init__(self, socketio):
    self.__socketio = socketio
    self.__tasks = []

  def add_task(self, task):
    self.__tasks.append(task)

  def execute(self):
    for task in self.__tasks:
      self.__socketio.emit('task_started', task.name, namespace='/sequence')
      try:
        task.execute()
      except Exception as exception:
        self.__socketio.emit('error', { 'task': task.name, 'message': str(exception) }, namespace='/sequence')
