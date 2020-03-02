from injector import inject
from src.domain.GlobalInfos import GlobalInfos
from src.domain.sequence.SequenceEventEmitter import SequenceEventEmitter
from src.domain.sequence.TaskContainer import TaskContainer


class MainTaskContainer(TaskContainer):

    @inject
    def __init__(self, global_infos: GlobalInfos, sequence_event_emitter: SequenceEventEmitter):
        super().__init__(global_infos, sequence_event_emitter)

        # TODO add tasks for the real sequence here
