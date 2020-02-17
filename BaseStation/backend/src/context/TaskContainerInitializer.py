from src.domain.sequence import TaskContainer
from src.domain.sequence.tasks import WarningExceptionTask, RetryableTask


class TaskContainerInitializer:

    def __init__(self, object_graph):
        self.object_graph = object_graph

    def populate_tasks(self, sequence_type):
        # switch sequence type and create tasks accordingly
        # exemple : main, robot_test, loops, errors, etc.
        # can be very usefull for creating small test sequences
        task_container = self.object_graph.provide(TaskContainer)

        if sequence_type == 'main':
            task_container.add_task(self.object_graph.provide(WarningExceptionTask))
            task_container.add_task(self.object_graph.provide(RetryableTask))
