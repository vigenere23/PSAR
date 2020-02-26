from src.domain import GlobalContext
from . import TaskContainer


class SequenceRunner:

    def __init__(
        self,
        global_context: GlobalContext,
        task_container: TaskContainer,
        thread_start,
        socket
    ):
        self.__global_context = global_context
        self.__task_container = task_container
        self.__thread_start = thread_start
        self.__socket = socket
        self.__sequence_thread = None

    def start(self, first_task=None):
        if not self.__sequence_thread or not self.__sequence_thread.is_alive():
            self.__sequence_thread = self.__thread_start(
                target=self.__task_container.execute, first_task=first_task
            )
            self.__sequence_thread.join()

    def stop(self):
        self.__socket.stop()

    def pause(self):
        self.__global_context.pause()

    def resume(self):
        self.__global_context.resume()
