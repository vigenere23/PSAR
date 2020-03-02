import time
from src.config import socketio_config
from src.app import socket
from src.context.interfaces import SocketHandlersContext


def connect_socket(connection_string, interval=0.5):
    while not socket.connected:
        try:
            socket.connect(connection_string)
        except Exception as exception:
            print(exception)
            print('Retrying connection in {} seconds'.format(interval))
            time.sleep(interval)


if __name__ == '__main__':
    SocketHandlersContext(socket).register()
    connection_string = "http://{}:{}".format(socketio_config['host'], socketio_config['port'])
    connect_socket(connection_string)
    print("I'm out!")
