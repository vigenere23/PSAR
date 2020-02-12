# needed for starting threads while using sockets...
# https://github.com/miguelgrinberg/Flask-SocketIO/issues/65
from gevent import monkey
monkey.patch_all()

from .app import app, socketio
from .config import socketio_config
from .context.interfaces.socket_handlers import SocketApiContext

SocketApiContext(socketio).register()

if __name__ == '__main__':
    socketio.run(
        app,
        host=socketio_config['host'],
        port=socketio_config['port']
    )
