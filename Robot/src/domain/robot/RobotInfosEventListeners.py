
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
from src.domain.stm.STMWriter import STMWriter


class RobotInfosEventListeners:
    @inject
    def __init__(self, robot_event_emitter: RobotEventEmitter, stm_writer: STMWriter, robot_infos: RobotInfos):
        self.__robot_event_emitter = robot_event_emitter
        self.__stm_writer = stm_writer
        self.__robot_infos = robot_infos

    def add_listeners(self):

        # Control BaseStation -> Robot
        self.__robot_infos.movement_observer.add_listener(self.__movement_listener)
        self.__robot_infos.gripper_control_observer.add_listener(self.__gripper_control_listener)
        self.__robot_infos.resistor_control_observer.add_listener(self.__resistor_control_listener)
        self.__robot_infos.puck_transporter_control_observer.add_listener(self.__puck_transporter_control_listener)
        self.__robot_infos.camera_observer.add_listener(self.__camera_listener)

        # Info   Robot -> BaseStation
        self.__robot_infos.powers_observer.add_listener(self.__powers_listener)
        self.__robot_infos.battery_observer.add_listener(self.__battery_listener)
        self.__robot_infos.gripper_info_observer.add_listener(self.__gripper_info_listener)
        self.__robot_infos.puck_transporter_info_observer.add_listener(self.__puck_transporter_info_listener)

    # Control BaseStation -> Robot

    def __movement_listener(self, robot_movement: RobotMovement):
        print(f"move: x: {robot_movement.x}, y: {robot_movement.y}")
        self.__stm_writer.send_move(robot_movement.x, robot_movement.y)
        print(f"rotate: rotation_speed: {robot_movement.rotation}")
        self.__stm_writer.send_rotate(robot_movement.rotation)

    def __gripper_control_listener(self, robot_gripper_control: RobotGripperControl):
        self.__stm_writer.send_gripper_status(robot_gripper_control.active)

    def __resistor_control_listener(self, resistor_control: ResistorControl):
        if resistor_control.start_measurement:
            self.__stm_writer.send_mesure_resistance()

    def __puck_transporter_control_listener(self, robot_puck_transporter_control: RobotPuckTransporterControl):
        # TODO implement this listener
        pass

    def __camera_listener(self, robot_camera: RobotCamera):
        # TODO implement this listener
        pass

    # Info  Robot -> BaseStation

    def __powers_listener(self, robot_powers: RobotPowers):
        self.__robot_event_emitter.send_powers(robot_powers)

    def __gripper_info_listener(self, robot_gripper_info: RobotGripperInfo):
        self.__robot_event_emitter.send_gripper_info(robot_gripper_info)

    def __puck_transporter_info_listener(self, robot_puck_transporter_info: RobotPuckTransporterInfo):
        self.__robot_event_emitter.send_puck_transporter_info(robot_puck_transporter_info)

    def __battery_listener(self, robot_battery: RobotBattery):
        self.__robot_event_emitter.send_battery(robot_battery)

    def __resistor_info_listener(self, resistor_info: ResistorInfo):
        self.__robot_event_emitter.send_resistor_info(resistor_info)
