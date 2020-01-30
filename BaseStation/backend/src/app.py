from flask import Flask
from flask_socketio import SocketIO
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*", ping_timeout=1, ping_interval=1)
