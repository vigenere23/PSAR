from flask import Flask, render_template
from flask_socketio import SocketIO, emit
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
SocketIO()
socketio = SocketIO(app, cors_allowed_origins="*", ping_timeout=1, ping_interval=1)
