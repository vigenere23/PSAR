from injector import inject
from socketio.client import Client
from src.domain.robot.Robot import Robot
from src.domain.robot.SerialPort import SerialPort
from src.domain.robot.RobotPower import RobotPower


class STMReader(object):

    @inject
    def __init__(self, socket: Client, robot: Robot, serial_port: SerialPort):
        """
        :param robot:
        :type robot: src.domain.robot.Robot.Robot
        :param serial_port:
        """
        self.__socket = socket
        self.__robot = robot
        self.__serial_port = serial_port
        self.read_thread = self.__socket.start_background_task(self.read_handler)

    def read_handler(self):
        while True:
            received_line = self.__serial_port.read_line()

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
