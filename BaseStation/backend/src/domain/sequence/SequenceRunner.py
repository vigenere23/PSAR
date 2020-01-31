from .SequenceThread import SequenceThread

class SequenceRunner:

  def __init__(self, task_container):
    self.__task_container = task_container
    self.__sequence_thread = None

  def start_sequence(self):
    if not self.__sequence_thread or not self.__sequence_thread.is_alive():
      self.__sequence_thread = SequenceThread(self.__task_container)
      self.__sequence_thread.start()
