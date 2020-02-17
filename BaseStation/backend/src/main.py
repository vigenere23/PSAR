# needed for starting threads while using sockets...
# https://github.com/miguelgrinberg/Flask-SocketIO/issues/65
from gevent import monkey
monkey.patch_all()

from pinject import new_object_graph
from .app import app, socketio
from .config import socketio_config
from .context import MainContext, SocketApiContext, TaskContainerInitializer

__context = MainContext(
    event_type='socket',
    event_instance=socketio,
    thread_starter=socketio.start_background_task
)

__object_graph = new_object_graph(binding_specs=[__context])
TaskContainerInitializer(__object_graph).populate_tasks('main')
SocketApiContext(__object_graph, socketio.on_namespace).register_routes()

if __name__ == '__main__':
    socketio.run(
        app,
        host=socketio_config['host'],
        port=socketio_config['port']
    )
