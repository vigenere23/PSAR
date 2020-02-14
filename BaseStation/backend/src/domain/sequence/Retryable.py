from .exceptions import RetryException


class Retryable:

    """
    Decorator that makes a task retryable.

    :param number_of_times:
    :type int:
        Number of times the task can retry.
        This number is reset each time a task succeeds or if
        the number of retries permitted has been reached.
        Note that the task will be run (number_of_times + 1) times in total.
    """
    def __init__(self, number_of_times: int):
        self.__initial_retries_left = number_of_times
        self.__retries_left = number_of_times

    """
    :raise RetryException: if the task should be retried
    :raise RuntimeError: if the number of retries has been exceeded
    """
    def __call__(self, f):
        def wrapper(*args, **kwargs):
            if self.__retries_left >= 0:
                self.__retries_left -= 1
                try:
                    value = f(*args, **kwargs)
                    self.__reset()
                    return value
                except Exception:
                    raise RetryException(self.__retries_left + 1)
            else:
                self.__reset()
                raise RuntimeError("Number of retries exceeded")
        return wrapper

    def __reset(self):
        self.__retries_left = self.__initial_retries_left
