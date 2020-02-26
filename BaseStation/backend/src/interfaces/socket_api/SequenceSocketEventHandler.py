from flask_socketio import Namespace


class SequenceSocketEventHandler(Namespace):

    def __init__(self, sequence_runner):
        super().__init__('/sequence')
        self.__sequence_runner = sequence_runner

    def on_start(self):
        self.__sequence_runner.start()

    def on_start_at_task(self, task):
        self.__sequence_runner.start(first_task=task)

    def on_stop(self):
        self.__sequence_runner.stop()

    def on_pause(self):
        self.__sequence_runner.pause()

    def on_resume(self):
        self.__sequence_runner.resume()
