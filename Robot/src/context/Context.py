from abc import ABC, abstractmethod


class Context(ABC):

    @abstractmethod
    def register(self):
        pass
