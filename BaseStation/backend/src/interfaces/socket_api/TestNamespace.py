from flask_socketio import Namespace, emit

class TestNamespace(Namespace):

    def __init__(self, namespace):
        super().__init__(namespace)

    def on_connect(self):
        print('Client connected!')

    def on_disconnect(self):
        print('Client disconnected')

    def on_request_event(self, message):
        data = 'Yes, yess, I received your message : {}'.format(message)
        emit('response_event', { 'data': data })
