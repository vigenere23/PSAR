from flask_socketio import Namespace
from injector import inject
from src.domain.robot.data_classes.RobotMovement import RobotMovement
from src.domain.robot.RobotInfos import RobotInfos


class DebugRobotSocketEventHandler(Namespace):

    @inject
    def __init__(self, robot_infos: RobotInfos):
        super().__init__('/debug_robot')
        self.__robot_infos = robot_infos

    def on_move(self, robot_movement_json: dict):
        robot_movement: RobotMovement = RobotMovement(**robot_movement_json)
        self.__robot_infos.movement = robot_movement
