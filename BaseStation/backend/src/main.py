from .app import app, socketio
from .context.interfaces import SocketApiContext

SocketApiContext(socketio).register()

if __name__ == '__main__':
  socketio.run(app)
