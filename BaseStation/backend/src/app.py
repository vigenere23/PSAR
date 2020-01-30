from flask import Flask
from flask_socketio import SocketIO
from .config import app_config
    
app = Flask(__name__)
app.config['SECRET_KEY'] = app_config['flask']['secret']

socketio = SocketIO(app, **app_config['socketio'])
