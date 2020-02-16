from src.domain.sequence import Retryable, Task
from src.domain.sequence.exceptions import RetryException

NUMBER_OF_RETRIES = 3


class RetryableTaskStub(Task):

    def __init__(self, fail_times=0, error=RetryException):
        self.__fail_times = fail_times
        self.__error = error
        self.execute_call_count = 0

    @Retryable(NUMBER_OF_RETRIES)
    def execute(self):
        self.execute_call_count += 1

        if self.__fail_times > 0:
            self.__fail_times -= 1
            raise self.__error()
