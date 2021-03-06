import logging
from src.domain.sequence.exceptions.RetryException import RetryException
from src.domain.sequence.exceptions.RetriesExceededException import RetriesExceededException


class Retryable:

    """
    Decorator that makes a task retryable.

    :param number_of_retries:
    :type int:
        Number of times the task can retry.
        This number is reset each time a task succeeds or if
        the number of retries permitted has been reached.
        Note that the task will be run (number_of_times + 1) times in total.
    """
    def __init__(self, number_of_retries: int):
        self.__number_of_retries = number_of_retries

    """
    :raise RetriesExceededException: if the number of retries has been exceeded
    """
    def __call__(self, f):
        def wrapper(*args, **kwargs):

            for i in range(self.__number_of_retries + 1, 0, -1):
                try:
                    return f(*args, **kwargs)
                except RetryException:
                    logging.info('Retrying task : {} retries left'.format(i - 1))

            raise RetriesExceededException(self.__number_of_retries)
        return wrapper
