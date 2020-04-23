from abc import ABC, abstractmethod


class SerialPort(ABC):

    @abstractmethod
    def write_line(self, text: str):
        pass

    @abstractmethod
    def read_line(self) -> str:
        pass
