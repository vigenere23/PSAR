from src.domain.sequence.Task import Task


class ErrorTask(Task):

    def execute(self):
        raise RuntimeError("Unprocessable data from world camera")
