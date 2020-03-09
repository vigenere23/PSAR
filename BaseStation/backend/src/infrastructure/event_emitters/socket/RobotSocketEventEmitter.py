from injector import inject
from flask_socketio import SocketIO
from socketio.exceptions import BadNamespaceError

from src.domain.robot.data_classes.Resistor import ResistorControl
from src.domain.robot.data_classes.RobotCamera import RobotCamera
from src.domain.robot.data_classes.RobotGripper import RobotGripperControl
from src.domain.robot.data_classes.RobotMovement import RobotMovement
from src.domain.robot.data_classes.RobotPuckTransporter import RobotPuckTransporterControl
from src.domain.robot.RobotEventEmitter import RobotEventEmitter


class RobotSocketEventEmitter(RobotEventEmitter):

    @inject
    def __init__(self, socket: SocketIO):
        self.__namespace = '/robot'
        self.__socket = socket

    def __emit(self, event, data=None, callback=None):
        try:
            self.__socket.emit(event, data, namespace=self.__namespace, callback=callback)
        except BadNamespaceError as e:
            print(f"emit error : {e}")

    def send_movement(self, robot_movement: RobotMovement):
        self.__emit('movement', robot_movement.to_json())

    def send_gripper_control(self, robot_gripper_control: RobotGripperControl):
        self.__emit('gripper_control', robot_gripper_control.to_json())

    def send_camera(self, robot_camera: RobotCamera):
        self.__emit('camera', robot_camera.to_json())

    def send_puck_transporter_control(self, robot_puck_transporter_control: RobotPuckTransporterControl):
        self.__emit('puck_transporter_control', robot_puck_transporter_control.to_json())

    def send_resistor_control(self, resistor_control: ResistorControl):
        self.__emit('resistor_control', resistor_control.to_json())
