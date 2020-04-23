from injector import inject
from src.domain.ThreadManager import ThreadManager


class GlobalInfos:

    @inject
    def __init__(self, thread_manager: ThreadManager):
        self.__thread_manager = thread_manager
        self.__paused = False

    def pause(self):
        print('PAUSING')
        self.__paused = True

    def resume(self):
        print("RESUMING")
        self.__paused = False

    def wait_until_resumed(self):
        while self.__paused:
            self.__thread_manager.sleep(1)
