from crc8 import crc8
from injector import inject
from socketio.client import Client
from src.domain.robot.RobotInfos import RobotInfos
from src.domain.robot.SerialPort import SerialPort
from src.domain.robot.data_classes.Resistor import ResistorInfo
from src.domain.robot.data_classes.RobotBattery import RobotBattery
from src.domain.robot.data_classes.RobotPowers import RobotPowers


class STMReader(object):

    @inject
    def __init__(self, socket: Client, robot_infos: RobotInfos, serial_port: SerialPort):
        self.__socket = socket
        self.__robot_infos = robot_infos
        self.__serial_port = serial_port
        self.read_thread = self.__socket.start_background_task(self.read_handler)

    def validate_checksum(self, message: str, checksum: str) -> bool:
        return self.generate_checksum(message) == checksum

    @staticmethod
    def generate_checksum(message: str) -> str:
        crc8_hash = crc8()
        crc8_hash.update(message.encode("utf8"))
        return crc8_hash.hexdigest()

    def read_valid_line(self) -> str:
        received_valid_line = False
        while not received_valid_line:
            received_line = self.__serial_port.read_line()
            message, checksum = received_line.split(";")
            received_valid_line = self.validate_checksum(message, checksum)
            if not received_valid_line:
                print("Invalid checksum")
            else:
                return message

    def read_handler(self):
        while True:
            received_line = self.read_valid_line()
            if "POWER" in received_line:
                received_line = received_line.replace("POWER:", "")
                powers = received_line.split(",")
                self.__robot_infos.powers = RobotPowers(*powers)
            elif "GRIPPER_PROXIMITY" in received_line:
                received_line = received_line.replace("GRIPPER_PROXIMITY:", "")
                gripper_making_contact = bool(received_line)
                current_gripper_info = self.__robot_infos.gripper_info
                current_gripper_info.making_contact = gripper_making_contact
                self.__robot_infos.gripper_info = current_gripper_info
            elif "RESISTOR" in received_line:
                received_line = received_line.replace("RESISTOR:", "")
                resistor = int(received_line)
                self.__robot_infos.resistor_info = ResistorInfo(resistor)
            elif "BATTERY" in received_line:
                received_line = received_line.replace("BATTERY:", "")
                battery_charge = int(received_line)
                self.__robot_infos.battery = RobotBattery(battery_charge)
            else:
                print("received from STM: {}".format(received_line))
