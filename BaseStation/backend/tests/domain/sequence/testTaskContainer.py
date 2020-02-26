from src.domain.sequence import TaskContainer
from tests import MockTestCase
from .stubs import TaskStub
from unittest.mock import Mock


class TaskContainerStub(TaskContainer):

    def __init__(self, sequence_event_emitter, tasks):
        super().__init__(Mock(), sequence_event_emitter)

        for task in tasks:
            self._add_task(task)


class TaskContainerTest(MockTestCase):

    def setUp(self):
        self.sequence_event_emitter = Mock()

    def test_when_executing_without_first_task_it_executes_all_tasks(self):
        tasks = self.__create_task_stubs(2)
        task_container = TaskContainerStub(self.sequence_event_emitter, tasks)

        task_container.execute()

        for task in tasks:
            self.assertCalledOnce(task.execute)

    def test_when_executing_with_first_task_it_executes_only_from_first_task(self):
        tasks = self.__create_task_stubs(3)
        tasks[1].name.return_value = 'FirstTask'
        task_container = TaskContainerStub(self.sequence_event_emitter, tasks)

        task_container.execute(first_task='FirstTask')

        self.assertNotCalled(tasks[0].execute)
        self.assertCalledOnce(tasks[1].execute)
        self.assertCalledOnce(tasks[2].execute)

    def __create_task_stubs(self, number_of_tasks):
        return [Mock(wraps=TaskStub()) for _ in range(number_of_tasks)]
