from abc import ABC, abstractmethod


class ThreadManager(ABC):

    @abstractmethod
    def sleep(self, seconds):
        pass

    @abstractmethod
    def start(self, *args, **kwargs):
        pass
