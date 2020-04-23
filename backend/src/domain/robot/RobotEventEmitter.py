from abc import ABC, abstractmethod

from src.domain.robot.data_classes.Resistor import ResistorControl
from src.domain.robot.data_classes.RobotCamera import RobotCamera
from src.domain.robot.data_classes.RobotGripper import RobotGripperControl
from src.domain.robot.data_classes.RobotMovement import RobotMovement
from src.domain.robot.data_classes.RobotPuckTransporter import RobotPuckTransporterControl


class RobotEventEmitter(ABC):

    @abstractmethod
    def send_movement(self, robot_movement: RobotMovement):
        pass

    @abstractmethod
    def send_gripper_control(self, robot_gripper: RobotGripperControl):
        pass

    @abstractmethod
    def send_camera(self, robot_camera: RobotCamera):
        pass

    @abstractmethod
    def send_puck_transporter_control(self, robot_puck_transporter_control: RobotPuckTransporterControl):
        pass

    @abstractmethod
    def send_resistor_control(self, resistor_control: ResistorControl):
        pass
