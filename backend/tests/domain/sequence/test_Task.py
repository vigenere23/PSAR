from unittest import TestCase
from .stubs import TaskStub


class TaskTest(TestCase):

    def test_name_should_be_class_name(self):
        task = TaskStub()
        self.assertEqual(task.name(), 'TaskStub')
