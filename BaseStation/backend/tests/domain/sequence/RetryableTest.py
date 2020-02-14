from unittest import TestCase
from src.domain.sequence import Task, Retryable
from src.domain.sequence.exceptions import RetryException

NUMBER_OF_RETRIES = 3


class TaskStub(Task):

    def __init__(self, should_fail=False):
        self.__should_fail = should_fail

    @Retryable(NUMBER_OF_RETRIES)
    def execute(self):
        if self.__should_fail:
            raise Exception()


class RetryableTest(TestCase):

    def test_failing_task_raises_retry_exception(self):
        task = TaskStub(should_fail=True)
        with self.assertRaises(RetryException):
            task.execute()

    def test_failing_task_raises_runtime_error_if_retries_exceeded(self):
        task = TaskStub(should_fail=True)

        for i in range(NUMBER_OF_RETRIES):
            with self.assertRaises(RetryException):
                task.execute()

        with self.assertRaises(RuntimeError):
            task.execute()

    def test_non_failing_task_should_not_raise_retry_exception(self):
        task = TaskStub()
        try:
            task.execute()
        except RetryException:
            self.fail("no RetryException should be raised")
