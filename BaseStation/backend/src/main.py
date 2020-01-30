from .app import app, socketio
from flask_socketio import emit
from .interfaces.socket_api import TestNamespace

@app.route('/')
def index():
  return (
    'Yes, it works... yeeaahh... ' +
    'Now try a socket connection and fire the event' +
    '\'request_event\' while listening to a \'response_event\'' +
    'and see if that works.'
  )

socketio.on_namespace(TestNamespace(''))

if __name__ == '__main__':
  socketio.run(app)
