class GlobalContext:

    def __init__(self, thread_sleep):
        self.__thread_sleep = thread_sleep
        self.__paused = False

    def pause(self):
        print('PAUSING')
        self.__paused = True

    def resume(self):
        print("RESUMING")
        self.__paused = False

    def wait_until_resumed(self):
        while self.__paused:
            self.__thread_sleep(1)
