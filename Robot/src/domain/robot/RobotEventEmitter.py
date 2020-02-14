from abc import ABC, abstractmethod


class RobotEventEmitter(ABC):

    @abstractmethod
    def send_resistance(self, resitance):
        pass
