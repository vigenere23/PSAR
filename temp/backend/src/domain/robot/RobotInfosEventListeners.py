
from injector import inject

from src.domain.robot.RobotEventEmitter import RobotEventEmitter
from src.domain.robot.RobotInfos import RobotInfos
from src.domain.robot.data_classes.Resistor import ResistorInfo, ResistorControl
from src.domain.robot.data_classes.RobotBattery import RobotBattery
from src.domain.robot.data_classes.RobotCamera import RobotCamera
from src.domain.robot.data_classes.RobotGripper import RobotGripperInfo, RobotGripperControl
from src.domain.robot.data_classes.RobotMovement import RobotMovement
from src.domain.robot.data_classes.RobotPowers import RobotPowers
from src.domain.robot.data_classes.RobotPuckTransporter import RobotPuckTransporterInfo, RobotPuckTransporterControl


class RobotInfosEventListeners:
    @inject
    def __init__(self, robot_event_emitter: RobotEventEmitter, robot_infos: RobotInfos):
        self.__robot_event_emitter = robot_event_emitter
        self.__robot_infos = robot_infos

    def add_listeners(self):

        # Control BaseStation -> Robot
        self.__robot_infos.movement_observer.add_listener(self.__movement_listener)
        self.__robot_infos.gripper_control_observer.add_listener(self.__gripper_control_listener)
        self.__robot_infos.resistor_info_observer.add_listener(self.__resistor_control_listener)
        self.__robot_infos.puck_transporter_control_observer.add_listener(self.__puck_transporter_control_listener)
        self.__robot_infos.camera_observer.add_listener(self.__camera_listener)

        # Info   Robot -> BaseStation
        self.__robot_infos.powers_observer.add_listener(self.__powers_listener)
        self.__robot_infos.battery_observer.add_listener(self.__battery_listener)
        self.__robot_infos.gripper_info_observer.add_listener(self.__gripper_info_listener)
        self.__robot_infos.puck_transporter_info_observer.add_listener(self.__puck_transporter_info_listener)

    # Control BaseStation -> Robot

    def __movement_listener(self, robot_movement: RobotMovement):
        self.__robot_event_emitter.send_movement(robot_movement)

    def __gripper_control_listener(self, robot_gripper_control: RobotGripperControl):
        self.__robot_event_emitter.send_gripper_control(robot_gripper_control)

    def __resistor_control_listener(self, resistor_control: ResistorControl):
        self.__robot_event_emitter.send_resistor_control(resistor_control)

    def __puck_transporter_control_listener(self, robot_puck_transporter_control: RobotPuckTransporterControl):
        self.__robot_event_emitter.send_puck_transporter_control(robot_puck_transporter_control)

    def __camera_listener(self, robot_camera: RobotCamera):
        self.__robot_event_emitter.send_camera(robot_camera)

    # Info   Robot -> BaseStation

    def __powers_listener(self, robot_powers: RobotPowers):
        # TODO implement this listener
        pass

    def __gripper_info_listener(self, robot_gripper_info: RobotGripperInfo):
        # TODO implement this listener
        pass

    def __puck_transporter_info_listener(self, robot_puck_transporter_info: RobotPuckTransporterInfo):
        # TODO implement this listener
        pass

    def __battery_listener(self, robot_battery: RobotBattery):
        # TODO implement this listener
        pass

    def __resistor_info_listener(self, resistor_info: ResistorInfo):
        # TODO implement this listener
        pass
