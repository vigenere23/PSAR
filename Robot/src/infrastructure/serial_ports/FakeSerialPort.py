from random import randrange
import random
from time import sleep
from collections import deque
from src.domain.robot.SerialPort import SerialPort
from threading import Thread
import crc8


class FakeSerialPort(SerialPort):
    def __init__(self, random_reception_generator=False):
        self.reception_buffer: deque[str] = deque([])
        if random_reception_generator:
            self.__random_reception_generator_thread = Thread(target=self.__random_reception_generator)
            self.__random_reception_generator_thread.daemon = True
            self.__random_reception_generator_thread.start()

    def write_line(self, text: str):
        print(f"Writing '{text}' to serial port")

    def __append_to_reception_buffer(self, reception_str: str):
        valid_checksum = randrange(1000)
        if valid_checksum:
            self.reception_buffer.append(f"{reception_str};{self.generate_checksum(reception_str)}")
        else:
            self.reception_buffer.append(f"{reception_str};{self.generate_checksum(reception_str+'!')}")

    def read_line(self) -> str:
        while len(self.reception_buffer) == 0:
            sleep(1)
        return self.reception_buffer.popleft()

    @staticmethod
    def generate_checksum(message: str) -> str:
        crc8_hash = crc8.crc8()
        crc8_hash.update(message.encode("utf8"))
        return crc8_hash.hexdigest()

    def __random_reception_generator(self):
        while True:
            random_command_number = randrange(4)
            if random_command_number == 0:
                random_command: str = f"POWER:{randrange(11)},{randrange(11)},{randrange(11)},{randrange(11)}," \
                                      f"{randrange(11)},{randrange(51)},{randrange(51)} "
            elif random_command_number == 1:
                random_command: str = f"GRIPPER_PROXIMITY:{random.choice([True, False])}"
            elif random_command_number == 2:
                random_command: str = f"RESISTOR:{randrange(100, 1000000)}"
            elif random_command_number == 3:
                random_command: str = f"BATTERY:{randrange(101)}"
            else:
                random_command: str = "error"
            self.__append_to_reception_buffer(random_command)
            sleep(randrange(0, 1))
