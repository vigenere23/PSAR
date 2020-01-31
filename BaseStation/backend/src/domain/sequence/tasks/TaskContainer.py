class TaskContainer:

  def __init__(self, socketio):
    self.__socketio = socketio
    self.__tasks = []

  def add_task(self, task):
    self.__tasks.append(task)

  def execute(self):
    for task in self.__tasks:
      self.__socketio.send("Task '{}' started...".format(task.name))
      task.execute()
      self.__socketio.send("Task '{}' ended.".format(task.name))
