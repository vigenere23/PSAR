from injector import inject
from socketio.client import Client
from socketio.exceptions import BadNamespaceError

from src.domain.robot.data_classes.Resistor import ResistorInfo
from src.domain.robot.data_classes.RobotBattery import RobotBattery
from src.domain.robot.data_classes.RobotGripper import RobotGripperInfo
from src.domain.robot.data_classes.RobotPowers import RobotPowers
from src.domain.robot.RobotEventEmitter import RobotEventEmitter
from src.domain.robot.data_classes.RobotPuckTransporter import RobotPuckTransporterInfo


class RobotSocketEventEmitter(RobotEventEmitter):

    @inject
    def __init__(self, socket: Client):
        self.__socket = socket
        self.__namespace = '/robot'

    def __emit(self, event, data=None, callback=None):
        try:
            self.__socket.emit(event, data, namespace=self.__namespace, callback=callback)
        except BadNamespaceError as e:
            print(f"emit error : {e}")

    def send_powers(self, robot_powers: RobotPowers):
        self.__emit('powers', robot_powers.to_json())

    def send_gripper_info(self, robot_gripper_info: RobotGripperInfo):
        self.__emit('gripper_info', robot_gripper_info.to_json())

    def send_puck_transporter_info(self, robot_puck_transporter_info: RobotPuckTransporterInfo):
        self.__emit('puck_transporter_info', robot_puck_transporter_info.to_json())

    def send_battery(self, robot_battery: RobotBattery):
        self.__emit('battery', robot_battery.to_json())

    def send_resistor_info(self, resistor_info: ResistorInfo):
        self.__emit('resistor_info', resistor_info.to_json())
