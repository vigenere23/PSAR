from .app import app, socketio
from flask_socketio import emit

@app.route('/')
def index():
  return (
    'Yes, it works... yeeaahh... ' +
    'Now try a socket connection and fire the event' +
    '\'request_event\' while listening to a \'response_event\'' +
    'and see if that works.'
  )

@socketio.on('connect')
def handle_connection():
  print('Client connected!')

@socketio.on('disconnect')
def handle_disconnection():
  print('Client disconnected')

@socketio.on('request_event')
def test_message(message):
  data = 'Yes, yess, I received your message : {}'.format(message)
  emit('response_event', { 'data': data })

if __name__ == '__main__':
  socketio.run(app)
