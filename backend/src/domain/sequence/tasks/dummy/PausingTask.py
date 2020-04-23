from injector import inject
from src.domain.GlobalInfos import GlobalInfos
from src.domain.sequence.Task import Task


class PausingTask(Task):

    @inject
    def __init__(self, global_infos: GlobalInfos):
        self.__global_infos = global_infos

    def execute(self):
        self.__global_infos.pause()
