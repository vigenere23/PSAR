from unittest import TestCase
from src.domain.sequence.exceptions.RetriesExceededException import RetriesExceededException
from .stubs.RetryableTaskStub import RetryableTaskStub, NUMBER_OF_RETRIES


class RetryableTest(TestCase):

    def test_given_task_not_raising_exception_when_executing_then_no_exception_is_raised(self):
        task = RetryableTaskStub(fail_times=0)

        try:
            task.execute()
        except Exception:
            self.fail('No error should be thrown')

    def test_given_task_that_keeps_failing_when_exceeding_retries_it_raises_retries_exceeded_exception(self):
        task = RetryableTaskStub(fail_times=NUMBER_OF_RETRIES + 1)

        with self.assertRaises(RetriesExceededException):
            task.execute()

    def test_given_task_that_keeps_failing_when_executing_it_should_only_retry_max_number_of_retries_times(self):
        task = RetryableTaskStub(fail_times=NUMBER_OF_RETRIES + 1)

        try:
            task.execute()
        except RetriesExceededException:
            self.assertEqual(task.execute_call_count, NUMBER_OF_RETRIES + 1)

    def test_given_task_that_fails_n_times_when_executing_it_should_only_retry_n_times(self):
        number_of_fails = NUMBER_OF_RETRIES - 1
        task = RetryableTaskStub(fail_times=number_of_fails)

        try:
            task.execute()
        except RetriesExceededException:
            self.assertEqual(task.execute_call_count, number_of_fails + 1)

    def test_given_task_that_raises_error_when_executing_it_does_not_catch_error(self):
        task = RetryableTaskStub(fail_times=NUMBER_OF_RETRIES + 1, error=Exception)

        with self.assertRaises(Exception):
            task.execute()
