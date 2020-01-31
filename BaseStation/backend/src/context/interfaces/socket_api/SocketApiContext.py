from src.context import Context
from src.interfaces.socket_api import TestNamespace, SequenceNamespace
from src.domain.sequence import SequenceRunner
from src.domain.sequence.tasks import TaskContainer, LoopTask

class SocketApiContext(Context):

  def __init__(self, socketio):
    self.__socketio = socketio

  def register(self):
    self.__socketio.on_namespace(TestNamespace(''))

    # TODO move this to specific contexts + use auto deps injection
    task_container = TaskContainer(self.__socketio)
    task_container.add_task(LoopTask(self.__socketio))
    task_container.add_task(LoopTask(self.__socketio))

    sequence_runner = SequenceRunner(task_container)
    sequence_namespace = SequenceNamespace('/sequence', sequence_runner)
    self.__socketio.on_namespace(sequence_namespace)
