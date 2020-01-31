class SequenceRunner:

  def __init__(self, socketio, sequence_thread):
    self.__sequence_thread = sequence_thread

  def start_sequence(self):
    if not self.__sequence_thread.is_alive():
      self.__sequence_thread.start()
      # I don't think we need a join here...
