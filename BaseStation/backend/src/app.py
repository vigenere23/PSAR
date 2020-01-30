from flask import Flask
from flask_socketio import SocketIO
from .config import flask_config, socketio_config

app = Flask(__name__)
app.config['SECRET_KEY'] = flask_config['secret']


socketio = SocketIO(
  app,
  ping_timeout=socketio_config['ping_timeout'],
  ping_interval=socketio_config['ping_interval'],
  cors_allowed_origins=socketio_config['cors_allowed_origins']
)
