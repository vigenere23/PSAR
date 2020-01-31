class SequenceRunner:

  def __init__(self, socketio, task_container):
    self.__socketio = socketio
    self.__task_container = task_container
    self.__sequence_thread = None

  def start_sequence(self):
    if not self.__sequence_thread or not self.__sequence_thread.is_alive():
      self.__sequence_thread = self.__socketio.start_background_task(target=self.__task_container.execute)
      self.__sequence_thread.join()
