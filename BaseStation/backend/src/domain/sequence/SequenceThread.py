from threading import Thread

class SequenceThread(Thread):

  def __init__(self, task_container):
    super().__init__(name='Sequence thread')
    self.__task_container = task_container

  def run(self):
    self.__task_container.execute()
    # TODO remove when solution is found
    raise RuntimeError()
