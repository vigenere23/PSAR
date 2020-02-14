from abc import ABC, abstractmethod


class Task(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def execute(self):
        pass
