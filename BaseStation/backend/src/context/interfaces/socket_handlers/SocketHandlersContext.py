from src.context import Context
from src.interfaces.socket_handlers import SequenceSocketEventHandler
from src.domain.sequence import SequenceRunner, TaskContainer
from src.domain.sequence.tasks import WarningExceptionTask, RetryableTask
from src.infrastructure.socket_emitters import SequenceSocketEventEmitter


class SocketHandlersContext(Context):

    def __init__(self, socketio):
        self.__socketio = socketio

    def register(self):
        # TODO move this to specific contexts + use auto deps injection
        sequence_event_emitter = SequenceSocketEventEmitter(self.__socketio)

        task_container = TaskContainer(sequence_event_emitter)
        task_container.add_task(WarningExceptionTask(self.__socketio))
        task_container.add_task(RetryableTask(self.__socketio))

        sequence_runner = SequenceRunner(
            task_container, self.__socketio.start_background_task
        )
        sequence_event_handler = SequenceSocketEventHandler(sequence_runner)
        self.__socketio.on_namespace(sequence_event_handler)
