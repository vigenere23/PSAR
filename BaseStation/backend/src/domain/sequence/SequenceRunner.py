class SequenceRunner:

    def __init__(self, task_container, thread_starter):
        self.__thread_starter = thread_starter
        self.__task_container = task_container
        self.__sequence_thread = None

    def start_sequence(self, first_task=None):
        if not self.__sequence_thread or not self.__sequence_thread.is_alive():
            self.__sequence_thread = self.__thread_starter(
                target=self.__task_container.execute, first_task=first_task
            )
            self.__sequence_thread.join()

    def stop_sequence(self):
        # TODO find a way to kill the sequence
        pass
