from unittest import TestCase
from src.domain.sequence import Task, Retryable
from src.domain.sequence.exceptions import RetriesExceededException


NUMBER_OF_RETRIES = 3


class RetryableTaskStub(Task):

    def __init__(self, should_fail=False):
        self.__should_fail = should_fail
        self.execute_call_count = 0

    @Retryable(NUMBER_OF_RETRIES)
    def execute(self):
        self.execute_call_count += 1
        if self.__should_fail:
            raise Exception()


class RetryableTest(TestCase):

    def test_non_failing_task_should_not_raise_retry_exception(self):
        task = RetryableTaskStub(should_fail=False)

        try:
            task.execute()
        except Exception:
            self.fail('No error should be thrown')

    def test_failing_task_raises_runtime_error_if_retries_exceeded(self):
        task = RetryableTaskStub(should_fail=True)

        with self.assertRaises(RetriesExceededException):
            task.execute()

    def test_failing_task_retries_only_number_of_retries_time(self):
        task = RetryableTaskStub(should_fail=True)

        try:
            task.execute()
        except RetriesExceededException:
            self.assertEqual(task.execute_call_count, NUMBER_OF_RETRIES + 1)
