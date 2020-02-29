from injector import inject
from src.domain.GlobalContext import GlobalContext
from src.domain.sequence.Task import Task


class PausingTask(Task):

    @inject
    def __init__(self, global_context: GlobalContext):
        self.__global_context = global_context

    def execute(self):
        self.__global_context.pause()
