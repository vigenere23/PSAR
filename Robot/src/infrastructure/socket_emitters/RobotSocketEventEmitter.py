from src.domain.robot import RobotEventEmitter


class RobotSocketEventEmitter(RobotEventEmitter):

    def __init__(self, socket):
        self.__socket = socket
        self.__namespace = '/robot'

    def send_resistance(self, resitance):
        # self.__socket.send('event_name', payload, namespace=self.__namespace)
        pass
