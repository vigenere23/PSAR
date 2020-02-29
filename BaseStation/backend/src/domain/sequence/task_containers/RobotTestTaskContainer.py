from injector import inject
from src.domain.GlobalContext import GlobalContext
from src.domain.sequence.SequenceEventEmitter import SequenceEventEmitter
from src.domain.sequence.TaskContainer import TaskContainer


class RobotTestTaskContainer(TaskContainer):

    @inject
    def __init__(self, global_context: GlobalContext, sequence_event_emitter: SequenceEventEmitter):
        super().__init__(global_context, sequence_event_emitter)

        # TODO add tasks for testing robot here
