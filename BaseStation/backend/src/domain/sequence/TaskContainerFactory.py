from src.domain.sequence.task_containers.MainTaskContainer import MainTaskContainer
from src.domain.sequence.task_containers.dummy.SpecialTasksTaskContainer import SpecialTasksTaskContainer
from src.domain.sequence.task_containers.dummy.RobotTestTaskContainer import RobotTestTaskContainer


class TaskContainerFactory:

    @staticmethod
    def get_class(name):
        if name == 'main':
            return MainTaskContainer
        elif name == 'robot':
            return RobotTestTaskContainer
        elif name == 'special-tasks':
            return SpecialTasksTaskContainer
        else:
            raise ValueError(
                "No task container available for type {}"
                .format(name)
            )
