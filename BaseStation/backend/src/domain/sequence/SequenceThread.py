from threading import Thread

class SequenceThread(Thread):

  def __init__(self, sequence_container):
    super().__init__()
    self.__sequence_container = sequence_container

  def run(self):
    self.__sequence_container.execute()
