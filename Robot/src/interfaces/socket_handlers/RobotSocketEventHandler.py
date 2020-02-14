from socketio import ClientNamespace


class RobotSocketEventHandler(ClientNamespace):

    def __init__(self):
        super().__init__('/robot')

    def on_move(self, move_info):
        pass
