from .. import TaskContainer


class MainTaskContainer(TaskContainer):

    def __init__(self, sequence_event_emitter, warning_exception_task, retryable_task):
        super().__init__(sequence_event_emitter)

        self._add_task(warning_exception_task)
        self._add_task(retryable_task)
