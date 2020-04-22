import socketio

socket = socketio.Client(reconnection_delay=0.5, reconnection_delay_max=0.5)


@socket.on('connect')
def connect_handler():
    print('Connection to BaseStation established!')

@socket.on('disconnect')
def disconnect_handler():
    print('Lost connection with BaseStation!')
