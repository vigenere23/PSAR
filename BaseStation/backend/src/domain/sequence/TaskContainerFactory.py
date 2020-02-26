from .task_containers import (
    MainTaskContainer,
    SpecialTasksTaskContainer,
    RobotTestTaskContainer
)


class TaskContainerFactory:

    def get_class(self, name):
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
