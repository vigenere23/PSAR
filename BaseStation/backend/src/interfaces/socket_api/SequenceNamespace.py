from flask_socketio import Namespace, emit
from flask_socketio import socketio

class SequenceNamespace(Namespace):

    def __init__(self, namespace, sequence_runner):
        super().__init__(namespace)
        self.__sequence_runner = sequence_runner

    def on_start(self):
        self.__sequence_runner.start_sequence()

    def on_start_at_task(self, task):
        self.__sequence_runner.start_sequence(first_task=task)

    def on_stop(self):
        self.__sequence_runner.stop_sequence()
