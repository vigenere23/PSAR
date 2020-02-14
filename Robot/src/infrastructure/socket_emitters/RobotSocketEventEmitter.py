from src.domain.robot import RobotEventEmitter


class RobotSocketEventEmitter(RobotEventEmitter):

    def __init__(self, socketio):
        self.__socketio = socketio
        self.__namespace = '/robot'

    def send_resistance(self, resitance):
        # self.__socketio.send('event_name', payload, namespace=self.__namespace)
        pass
