from abc import ABC, abstractmethod


class SequenceEventEmitter(ABC):

    @abstractmethod
    def send_task_started(self, task_name):
        pass

    @abstractmethod
    def send_sequence_ended(self):
        pass

    @abstractmethod
    def send_task_warning(self, task_name, message):
        pass

    @abstractmethod
    def send_task_error(self, task_name, message):
        pass

    @abstractmethod
    def send_task_retry(self, task_name):
        pass
