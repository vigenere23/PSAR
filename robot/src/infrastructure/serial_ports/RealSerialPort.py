from serial import Serial
from src.domain.robot.SerialPort import SerialPort


class RealSerialPort(SerialPort):

    __DEFAULT_BAUDRATE = 19200

    def __init__(self, port_name: str):
        self.__serial_com = Serial(port_name)
        self.__serial_com.baudrate = self.__DEFAULT_BAUDRATE

    def write_line(self, text: str):
        encoded_text = f"{text}\n".encode('utf-8')
        return self.__serial_com.write(encoded_text)

    def read_line(self) -> str:
        text = self.__serial_com.readline()
        return text.decode(encoding='utf8', errors='ignore')
