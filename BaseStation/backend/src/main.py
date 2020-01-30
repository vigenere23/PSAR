from .app import app, socketio
from .config import socketio_config
from .context.interfaces.socket_api import SocketApiContext

SocketApiContext(socketio).register()

if __name__ == '__main__':
  socketio.run(
    app,
    host=socketio_config['host'],
    port=socketio_config['port']
  )
