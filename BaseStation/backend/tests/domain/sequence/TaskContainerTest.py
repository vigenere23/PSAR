from src.domain.sequence import TaskContainer
from tests import MockTestCase
from .stubs import TaskStub
from unittest.mock import Mock


class TaskContainerTest(MockTestCase):

    def setUp(self):
        sequence_event_emitter = Mock()
        self.task_container = TaskContainer(sequence_event_emitter)

    def test_when_executing_without_first_task_it_executes_all_tasks(self):
        tasks = self.__create_task_stubs(2)
        self.__add_tasks_to_container(tasks)

        self.task_container.execute()

        for task in tasks:
            self.assertCalledOnce(task.execute)

    def test_when_executing_with_first_task_it_executes_only_from_first_task(self):
        tasks = self.__create_task_stubs(3)
        tasks[1].name.return_value = 'FirstTask'
        self.__add_tasks_to_container(tasks)

        self.task_container.execute(first_task='FirstTask')

        self.assertNotCalled(tasks[0].execute)
        self.assertCalledOnce(tasks[1].execute)
        self.assertCalledOnce(tasks[2].execute)

    def __create_task_stubs(self, number_of_tasks):
        return [Mock(wraps=TaskStub()) for _ in range(number_of_tasks)]

    def __add_tasks_to_container(self, tasks):
        for task in tasks:
            self.task_container.add_task(task)
