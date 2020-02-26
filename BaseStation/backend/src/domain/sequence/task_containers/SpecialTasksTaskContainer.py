from .. import TaskContainer
from src.domain.sequence import SequenceEventEmitter
from src.domain.sequence.tasks import PausingTask, RetryableTask, WarningExceptionTask


class SpecialTasksTaskContainer(TaskContainer):

    def __init__(
        self,
        global_context,
        sequence_event_emitter: SequenceEventEmitter,
        pausing_task: PausingTask,
        warning_exception_task: WarningExceptionTask,
        retryable_task: RetryableTask
    ):
        super().__init__(global_context, sequence_event_emitter)

        self._add_task(warning_exception_task)
        self._add_task(pausing_task)
        self._add_task(retryable_task)
