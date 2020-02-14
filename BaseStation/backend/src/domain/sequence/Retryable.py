from .exceptions import RetryException


class Retryable:

    def __init__(self, number_of_times):
        self.__initial_retries_left = number_of_times
        self.__retries_left = number_of_times

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
