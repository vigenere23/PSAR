from injector import Module, Binder
from src.domain.robot.RobotInfos import RobotInfos


class RobotInstanceContext(Module):

    def __init__(self, robot_infos_instance: RobotInfos):
        self.__robot_infos_instance = robot_infos_instance

    def configure(self, binder: Binder):
        binder.bind(RobotInfos, to=self.__robot_infos_instance)
