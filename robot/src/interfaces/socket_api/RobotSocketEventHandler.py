from injector import inject
from socketio import ClientNamespace

from src.domain.robot.RobotInfos import RobotInfos
from src.domain.robot.data_classes.Resistor import ResistorControl
from src.domain.robot.data_classes.RobotCamera import RobotCamera
from src.domain.robot.data_classes.RobotGripper import RobotGripperControl
from src.domain.robot.data_classes.RobotMovement import RobotMovement
from src.domain.robot.data_classes.RobotPuckTransporter import RobotPuckTransporterControl


class RobotSocketEventHandler(ClientNamespace):

    @inject
    def __init__(self, robot_infos: RobotInfos):
        super().__init__('/robot')
        self.__robot_infos = robot_infos

    def on_connect(self):
        print("robot_connected")
        self.__robot_infos.gripper_info_observer.trig_listeners_with_last_event()
        self.__robot_infos.puck_transporter_info_observer.trig_listeners_with_last_event()
        self.__robot_infos.resistor_info_observer.trig_listeners_with_last_event()

    def on_movement(self, robot_movement_json: str):
        robot_movement = RobotMovement.from_json(robot_movement_json)
        self.__robot_infos.movement = robot_movement

    def on_gripper_control(self, robot_gripper_control_json: str):
        robot_gripper_control = RobotGripperControl.from_json(robot_gripper_control_json)
        self.__robot_infos.gripper_control = robot_gripper_control

    def on_camera(self, robot_camera_json: str):
        robot_camera = RobotCamera.from_json(robot_camera_json)
        self.__robot_infos.camera = robot_camera

    def on_puck_transporter_control(self, robot_puck_transporter_control_json: str):
        robot_puck_transporter_control = RobotPuckTransporterControl.from_json(
            robot_puck_transporter_control_json)
        self.__robot_infos.puck_transporter_control = robot_puck_transporter_control

    def on_resistor_control(self, resistor_control_json: str):
        resistor_control = ResistorControl.from_json(resistor_control_json)
        self.__robot_infos.resistor_control = resistor_control
