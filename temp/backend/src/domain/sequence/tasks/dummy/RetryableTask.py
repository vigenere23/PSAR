from injector import inject
from src.domain.GeneralEventEmitter import GeneralEventEmitter
from src.domain.ThreadManager import ThreadManager
from src.domain.sequence.Task import Task
from src.domain.sequence.Retryable import Retryable


class RetryableTask(Task):

    @inject
    def __init__(self, thread_manager: ThreadManager, general_event_emitter: GeneralEventEmitter):
        self.__thread_manager = thread_manager
        self.__general_event_emitter = general_event_emitter

    @Retryable(5)
    def execute(self):
        self.__thread_manager.sleep(1)
        self.__general_event_emitter.send_message('... doing something')
        self.retry()
