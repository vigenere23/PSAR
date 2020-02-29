from injector import inject
from src.domain.GlobalContext import GlobalContext
from src.domain.ThreadManager import ThreadManager
from src.domain.sequence.TaskContainer import TaskContainer


class SequenceRunner:

    @inject
    def __init__(
        self,
        global_context: GlobalContext,
        task_container: TaskContainer,
        thread_manager: ThreadManager
    ):
        self.__global_context = global_context
        self.__task_container = task_container
        self.__thread_manager = thread_manager
        self.__sequence_thread = None

    def start(self, first_task=None):
        if not self.__sequence_thread or not self.__sequence_thread.is_alive():
            self.__sequence_thread = self.__thread_manager.start(
                target=self.__task_container.execute, first_task=first_task
            )
            self.__sequence_thread.join()

    def stop(self):
        # TODO
        pass

    def pause(self):
        self.__global_context.pause()

    def resume(self):
        self.__global_context.resume()
