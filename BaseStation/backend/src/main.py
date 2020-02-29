# needed for starting threads while using sockets...
# https://github.com/miguelgrinberg/Flask-SocketIO/issues/65
from gevent import monkey
monkey.patch_all()

from src.app import app, socket
from src.config import socketio_config
from injector import Injector
from src.context.MainContext import MainContext
from src.context.SocketApiContext import SocketApiContext

injector = Injector(modules=[MainContext(event_instance=socket)])
SocketApiContext(injector, socket.on_namespace).register_routes()

if __name__ == '__main__':
    socket.run(
        app,
        host=socketio_config['host'],
        port=socketio_config['port']
    )
