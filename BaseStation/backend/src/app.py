from flask import Flask
from flask_socketio import SocketIO
from src.config import flask_config

app = Flask(__name__)
app.config['SECRET_KEY'] = flask_config['secret']
app.env = flask_config['env']
app.debug = flask_config['debug']


socket = SocketIO(app, cors_allowed_origins='*', always_connect=True)
