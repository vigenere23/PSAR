from src.domain.sequence import TaskContainer
from src.domain.sequence.tasks import WarningExceptionTask, RetryableTask


class TaskContainerInitializer:

    def __init__(self, object_graph, event_instance):
        self.object_graph = object_graph
        self.event_instance = event_instance

    def populate_tasks(self, sequence_type):
        # switch sequence type and create tasks accordingly
        # exemple : main, robot_test, loops, errors, etc.
        # can be very usefull for creating small test sequences
        task_container = self.object_graph.provide(TaskContainer)

        if sequence_type == 'main':
            task_container.add_task(WarningExceptionTask(self.event_instance))
            task_container.add_task(RetryableTask(self.event_instance))
