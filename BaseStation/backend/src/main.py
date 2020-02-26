# needed for starting threads while using sockets...
# https://github.com/miguelgrinberg/Flask-SocketIO/issues/65
from gevent import monkey
monkey.patch_all()

from .app import app, socket
from .domain import GlobalContext
from .config import socketio_config
from pinject import new_object_graph
from .context import MainContext, SocketApiContext

__context = MainContext(
    event_instance=socket,
    thread_start=socket.start_background_task,
    thread_sleep=socket.sleep,
    global_context=GlobalContext(socket.sleep)
)

__object_graph = new_object_graph(binding_specs=[__context])
SocketApiContext(__object_graph, socket.on_namespace).register_routes()

if __name__ == '__main__':
    socket.run(
        app,
        host=socketio_config['host'],
        port=socketio_config['port']
    )
