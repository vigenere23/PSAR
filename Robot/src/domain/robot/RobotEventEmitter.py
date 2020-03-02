from abc import ABC, abstractmethod

from src.domain.data_classes.Resistor import ResistorInfo
from src.domain.data_classes.RobotBattery import RobotBattery
from src.domain.data_classes.RobotGripper import RobotGripperInfo
from src.domain.data_classes.RobotPowers import RobotPowers


class RobotEventEmitter(ABC):

    @abstractmethod
    def send_powers(self, robot_powers: RobotPowers):
        pass

    @abstractmethod
    def send_gripper_info(self, robot_gripper_info: RobotGripperInfo):
        pass

    @abstractmethod
    def send_battery(self, robot_battery: RobotBattery):
        pass

    @abstractmethod
    def send_resistor_info(self, resistor_info: ResistorInfo):
        pass
