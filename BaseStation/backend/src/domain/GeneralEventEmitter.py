from abc import ABC, abstractmethod


class GeneralEventEmitter(ABC):

    @abstractmethod
    def send_message(self, message):
        pass
