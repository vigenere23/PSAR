from .. import Task
from ..exceptions import WarningException


class WarningExceptionTask(Task):

    def __init__(self, socket):
        self.__socket = socket

    def execute(self):
        self.__socket.sleep(1)
        self.__socket.send('... doing somethig')
        raise WarningException(
            "Can no longer see puck - maybe the robot is colliding with it?"
        )
