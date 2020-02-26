from .. import TaskContainer
from src.domain.sequence import SequenceEventEmitter


class RobotTestTaskContainer(TaskContainer):

    def __init__(
        self,
        global_context,
        sequence_event_emitter: SequenceEventEmitter
    ):
        super().__init__(global_context, sequence_event_emitter)

        # TODO add tasks for testing robot here
