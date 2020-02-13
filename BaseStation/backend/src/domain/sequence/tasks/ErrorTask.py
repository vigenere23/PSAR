from .. import Task


class ErrorTask(Task):

    def __init__(self):
        super().__init__('Error')

    def execute(self):
        raise RuntimeError("Unprocessable data from world camera")
