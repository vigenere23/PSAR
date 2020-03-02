from injector import inject
from flask_socketio import SocketIO

from src.domain.data_classes.Resistor import ResistorControl
from src.domain.data_classes.RobotCamera import RobotCamera
from src.domain.data_classes.RobotGripper import RobotGripperControl
from src.domain.data_classes.RobotMovement import RobotMovement
from src.domain.data_classes.RobotPuckTransporter import RobotPuckTransporterControl
from src.domain.robot.RobotEventEmitter import RobotEventEmitter


class RobotSocketEventEmitter(RobotEventEmitter):

    @inject
    def __init__(self, socket: SocketIO):
        self.__namespace = '/robot'
        self.__socket = socket

    def send_movement(self, robot_movement: RobotMovement):
        self.__socket.emit('movement', robot_movement.to_json(), namespace=self.__namespace)

    def send_gripper_control(self, robot_gripper_control: RobotGripperControl):
        self.__socket.emit('gripper_control', robot_gripper_control.to_json(), namespace=self.__namespace)

    def send_camera(self, robot_camera: RobotCamera):
        self.__socket.emit('camera', robot_camera.to_json(), namespace=self.__namespace)

    def send_puck_transporter_control(self, robot_puck_transporter_control: RobotPuckTransporterControl):
        self.__socket.emit('puck_transporter_control', robot_puck_transporter_control.to_json(),
                           namespace=self.__namespace)

    def send_resistor_control(self, resistor_control: ResistorControl):
        self.__socket.emit('resistor_control', resistor_control.to_json(), namespace=self.__namespace)
