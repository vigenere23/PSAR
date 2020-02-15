from .. import Task
from ..exceptions import WarningException


class WarningExceptionTask(Task):

    def __init__(self, socketio):
        self.__socketio = socketio

    def execute(self):
        self.__socketio.sleep(1)
        self.__socketio.send('... doing somethig')
        raise WarningException(
            "Can no longer see puck - maybe the robot is colliding with it?"
        )
