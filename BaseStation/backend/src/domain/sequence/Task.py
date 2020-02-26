from abc import ABC, abstractmethod
from .exceptions import RetryException


class Task(ABC):

    def name(self):
        return self.__class__.__name__

    def retry(self):
        raise RetryException(self.name())

    @abstractmethod
    def execute(self):
        pass
