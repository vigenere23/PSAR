from .. import Task


class ErrorTask(Task):

    def execute(self):
        raise RuntimeError("Unprocessable data from world camera")
