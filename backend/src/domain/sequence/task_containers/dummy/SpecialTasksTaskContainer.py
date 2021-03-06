from injector import inject
from src.domain.GlobalInfos import GlobalInfos
from src.domain.sequence.SequenceEventEmitter import SequenceEventEmitter
from src.domain.sequence.tasks.dummy.PausingTask import PausingTask
from src.domain.sequence.tasks.dummy.RetryableTask import RetryableTask
from src.domain.sequence.tasks.dummy.WarningExceptionTask import WarningExceptionTask
from src.domain.sequence.TaskContainer import TaskContainer


class SpecialTasksTaskContainer(TaskContainer):

    @inject
    def __init__(
            self,
            global_infos: GlobalInfos,
            sequence_event_emitter: SequenceEventEmitter,
            pausing_task: PausingTask,
            warning_exception_task: WarningExceptionTask,
            retryable_task: RetryableTask
    ):
        super().__init__(global_infos, sequence_event_emitter)

        self._add_task(warning_exception_task)
        self._add_task(pausing_task)
        self._add_task(retryable_task)
