# needed for starting threads while using sockets...
# https://github.com/miguelgrinberg/Flask-SocketIO/issues/65
from gevent import monkey
monkey.patch_all()

from pinject import new_object_graph
from .app import app, socketio
from .config import socketio_config
from .context import MainContext, EventHandlersRegisterer, TaskContainerInitializer

__context = MainContext(event_type='socket', event_instance=socketio)

__object_graph = new_object_graph(binding_specs=[__context])
EventHandlersRegisterer(__object_graph, socketio.on_namespace)
TaskContainerInitializer(__object_graph, socketio).populate_tasks('main')

if __name__ == '__main__':
    socketio.run(
        app,
        host=socketio_config['host'],
        port=socketio_config['port']
    )
