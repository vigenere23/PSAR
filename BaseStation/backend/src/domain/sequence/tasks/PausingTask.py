from .. import Task


class PausingTask(Task):

    def __init__(self, global_context):
        self.__global_context = global_context

    def execute(self):
        self.__global_context.pause()
