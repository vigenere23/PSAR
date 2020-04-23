from injector import Module, Binder

from src.context.RobotInstanceContext import RobotInstanceContext
# from src.context.ThreadManagerContext import ThreadManagerContext
from src.context.SequenceContext import SequenceContext
from src.context.EventEmittersContext import EventEmittersContext
from src.context.EventInstanceContext import EventInstanceContext
from src.domain.GlobalInfos import GlobalInfos
from src.domain.ThreadManager import ThreadManager
from src.infrastructure.thread_managers.SocketThreadManager import SocketThreadManager
from src.domain.robot.RobotInfos import RobotInfos


class MainContext(Module):

    def __init__(self, event_instance=None):
        super().__init__()
        self.__event_instance = event_instance

    def configure(self, binder: Binder):
        binder.install(EventInstanceContext(self.__event_instance))
        binder.install(EventEmittersContext())
        # binder.install(ThreadManagerContext())

        # TODO fix this -> global_context seems to exists once PER THREAD
        socket_thread_manager = SocketThreadManager(self.__event_instance)
        global_infos = GlobalInfos(socket_thread_manager)
        binder.bind(ThreadManager, to=socket_thread_manager)
        binder.bind(GlobalInfos, to=global_infos)

        binder.install(RobotInstanceContext(RobotInfos()))
        binder.install(SequenceContext())
