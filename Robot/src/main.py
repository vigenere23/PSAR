import time
from injector import Injector
from src.config import socketio_config
from src.app import socket
from src.context.SocketApiContext import SocketApiContext
from src.context.MainContext import MainContext


def connect_socket(connection_string, interval=0.5):
    while not socket.connected:
        try:
            socket.connect(connection_string)
        except Exception as exception:
            print(exception)
            print(f'Retrying connection in {interval} seconds')
            time.sleep(interval)


if __name__ == '__main__':
    injector = Injector(modules=[MainContext(event_instance=socket)])
    SocketApiContext(injector, socket.register_namespace).register_routes()

    connection_string = f"http://{socketio_config['host']}:{socketio_config['port']}"
    connect_socket(connection_string)
