from flask_socketio import Namespace, emit

class SequenceNamespace(Namespace):

  def __init__(self, namespace, sequence_runner):
    super().__init__(namespace)
    self.__sequence_runner = sequence_runner

  def on_start(self):
    self.__sequence_runner.start_sequence()
