import time
from .config import socketio_config
from .app import socket
from .context.interfaces import SocketHandlersContext


def connect_socket(connection_string, interval=2):
    connected = False

    while not connected:
        try:
            socket.connect(connection_string)
            connected = True
            print('Successfuly connected')
        except Exception as exception:
            print(exception)
            print('Retrying connection in {} seconds'.format(interval))
            time.sleep(interval)


if __name__ == '__main__':
    SocketHandlersContext(socket).register()

    connection_string = "http://{}:{}".format(socketio_config['host'], socketio_config['port'])
    connect_socket(connection_string)