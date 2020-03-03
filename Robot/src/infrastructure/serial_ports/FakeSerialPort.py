from src.domain.robot.SerialPort import SerialPort


class FakeSerialPort(SerialPort):

    def write_line(self, text: str):
        print(f'Writing \'{text}\' to serial port')

    def read_line(self) -> str:
        return 'I\'m a fake serial port, nothing to read here\n'
