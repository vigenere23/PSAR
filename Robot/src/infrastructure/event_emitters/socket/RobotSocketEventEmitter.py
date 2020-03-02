from src.domain.data_classes.Resistor import ResistorInfo
from src.domain.data_classes.RobotBattery import RobotBattery
from src.domain.data_classes.RobotGripper import RobotGripperInfo
from src.domain.data_classes.RobotPowers import RobotPowers
from src.domain.robot.RobotEventEmitter import RobotEventEmitter


class RobotSocketEventEmitter(RobotEventEmitter):

    def __init__(self, socket):
        self.__socket = socket
        self.__namespace = '/robot'

    def send_powers(self, robot_powers: RobotPowers):
        self.__socket.emit('powers', robot_powers.to_json(), namespace=self.__namespace)

    def send_gripper_info(self, robot_gripper_info: RobotGripperInfo):
        self.__socket.emit('gripper_info', robot_gripper_info.to_json(), namespace=self.__namespace)

    def send_battery(self, robot_battery: RobotBattery):
        self.__socket.emit('battery', robot_battery.to_json(), namespace=self.__namespace)

    def send_resistor_info(self, resistor_info: ResistorInfo):
        self.__socket.emit('resistor_info', resistor_info.to_json(), namespace=self.__namespace)
