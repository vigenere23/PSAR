from injector import inject
from src.domain.ThreadManager import ThreadManager
from src.domain.robot.data_classes.RobotMovement import RobotMovement
from src.domain.robot.RobotInfos import RobotInfos
from src.domain.sequence.Task import Task


class RobotMoveSquareTask(Task):
    @inject
    def __init__(self, thread_manager: ThreadManager, robot_infos: RobotInfos):
        self.__thread_manager = thread_manager
        self.__robot_infos = robot_infos

    def execute(self):
        print(self.__robot_infos.movement.x)
        self.__robot_infos.movement = RobotMovement(50, 0, 0)
        self.__thread_manager.sleep(1)
        self.__robot_infos.movement = RobotMovement(0, 50, 0)
        self.__thread_manager.sleep(1)
        self.__robot_infos.movement = RobotMovement(-50, 0, 0)
        self.__thread_manager.sleep(1)
        self.__robot_infos.movement = RobotMovement(0, -50, 0)
        self.__thread_manager.sleep(1)
        self.__robot_infos.movement = RobotMovement(0, 0, 0)

