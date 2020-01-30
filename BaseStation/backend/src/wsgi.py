import os
from .config import socketio_config

connection_string = '{}:{}'.format(socketio_config['host'], socketio_config['port'])

os.system('uwsgi --socket {} --protocol=http --enable-threads -w src.main:app'.format(connection_string))
