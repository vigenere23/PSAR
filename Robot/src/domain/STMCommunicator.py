import threading
import time
from src.app import socket
from src.domain.robot.RobotPower import RobotPower


class STMCommunicator(object):
    def __init__(self, robot, serial):
        """
        :param robot:
        :type robot: src.domain.robot.Robot.Robot
        :param serial:
        """
        self.__robot = robot
        self.__serial = serial
        self.__serial.baudrate = 19200
        self.read_thread = socket.start_background_task(self.read_handler)
        self.last_x_received = 0
        self.last_y_received = 0
        self.lock = threading.Lock()

    def __send(self, string_to_send: str):
        self.__serial.write("{}\n".format(string_to_send).encode('utf-8'))

    def move(self, x: int, y: int):
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
            self.__send("MOVE:{},{}".format(x, y))
        self.lock.release()

    def rotate(self, rotate_speed: int):
        """
        Send via UART the ROTATE command with the rotation speed
        :param rotate_speed: Speed to turn from -100 to 100. Negative -> CCW, Positive -> CW
        """
        rotate_speed = max(min(rotate_speed, 100), -100)
        self.__send("ROTATE:{},0".format(rotate_speed))

    def resistor_measurement(self):
        """
        Send via UART the RESISTOR command to initiate the resistor measurement
        """
        self.__send("RESISTOR:0,0")

    def gripper(self, state: bool):
        """
        Send via UART the GRIPPER command to set the state of the electromagnet
        :param state: state of the electromagnet. (True: ON, False: OFF)
        """
        self.__send("GRIPPER:{},0".format(int(state)))

    def read_handler(self):
        while True:
            received_line = self.__serial.readline().decode(encoding="utf8", errors="ignore")

            if "POWER" in received_line:
                received_line = received_line.replace("POWER:", "")
                powers = received_line.split(",")
                self.__robot.powers = RobotPower(*powers)
            elif "GRIPPER_PROXIMITY" in received_line:
                self.__robot.gripper_proximity = "1" in received_line
            elif "RESISTOR" in received_line:
                received_line = received_line.replace("RESISTOR:", "")
                resistor = int(received_line)
                self.__robot.resistor = resistor
            # elif "SPEED" in received_line:
            #     received_line = received_line.replace("SPEED:", "")
            #     print("{} {}".format(time.time(), received_line))
            else:
                print("received from STM: {}".format(received_line))
