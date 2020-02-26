from .. import TaskContainer
from src.domain.sequence import SequenceEventEmitter
from src.domain.sequence.tasks import RetryableTask, WarningExceptionTask


class MainTaskContainer(TaskContainer):

    def __init__(
        self,
        sequence_event_emitter: SequenceEventEmitter,
        warning_exception_task: WarningExceptionTask,
        retryable_task: RetryableTask
    ):
        super().__init__(sequence_event_emitter)

        self._add_task(warning_exception_task)
        self._add_task(retryable_task)
