from src.domain.sequence import Retryable, Task

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
