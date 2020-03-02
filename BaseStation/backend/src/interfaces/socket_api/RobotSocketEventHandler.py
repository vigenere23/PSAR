from injector import inject
from flask_socketio import Namespace
from flask_socketio import SocketIO

from src.domain.data_classes.Resistor import ResistorInfo
from src.domain.data_classes.RobotBattery import RobotBattery
from src.domain.data_classes.RobotGripper import RobotGripperInfo
from src.domain.data_classes.RobotPowers import RobotPowers
from src.domain.robot.RobotInfos import RobotInfos


class RobotSocketEventHandler(Namespace):

    @inject
    def __init__(self, robot_infos: RobotInfos):
        super().__init__('/robot')
        self.__robot_infos = robot_infos

    def on_powers(self, robot_powers_json: str):
        robot_powers: RobotPowers = RobotPowers.from_json(robot_powers_json)
        self.__robot_infos.powers = robot_powers

    def on_gripper_info(self, robot_gripper_info_json: str):
        robot_gripper_info: RobotGripperInfo = RobotGripperInfo.from_json(robot_gripper_info_json)
        self.__robot_infos.gripper_info = robot_gripper_info

    def on_battery(self, robot_battery_json: str):
        robot_battery: RobotBattery = RobotBattery.from_json(robot_battery_json)
        self.__robot_infos.battery = robot_battery

    def on_resistor_info(self, resistor_info_json: str):
        resistor_info: ResistorInfo = ResistorInfo.from_json(resistor_info_json)
        # todo handle resistor value

