import threading
from injector import inject
from src.domain.robot.SerialPort import SerialPort


class STMWriter(object):

    @inject
    def __init__(self, serial_port: SerialPort):
        """
        :param robot:
        :type robot: src.domain.robot.Robot.Robot
        :param serial_port:
        """
        self.__serial_port = serial_port
        self.last_x_received = 0
        self.last_y_received = 0
        self.lock = threading.Lock()

    def send_move(self, x: int, y: int):
        """
        Send via UART the MOVE command with x and y cartesian projection of the direction vector
        :param x: Speed of movement in X axis from -100 to 100
        :param y: Speed of movement in Y axis from -100 to 100
        """
        # todo Raise exception or min max
        x = max(min(x, 100), -100)
        y = max(min(y, 100), -100)
        self.last_x_received = x
        self.last_y_received = y
        self.lock.acquire()
        if self.last_x_received == x and self.last_y_received == y:
            self.__serial_port.write_line(f'MOVE:{x},{y}')
        self.lock.release()

    def send_rotate(self, rotate_speed: int):
        """
        Send via UART the ROTATE command with the rotation speed
        :param rotate_speed: Speed to turn from -100 to 100. Negative -> CCW, Positive -> CW
        """
        rotate_speed = max(min(rotate_speed, 100), -100)
        self.__serial_port.write_line(f'ROTATE:{rotate_speed},0')

    def send_mesure_resistance(self):
        """
        Send via UART the RESISTOR command to initiate the resistor measurement
        """
        self.__serial_port.write_line('RESISTOR:0,0')

    def send_gripper_status(self, state: bool):
        """
        Send via UART the GRIPPER command to set the state of the electromagnet
        :param state: state of the electromagnet. (True: ON, False: OFF)
        """
        self.__serial_port.write_line(f'GRIPPER:{int(state)},0')
