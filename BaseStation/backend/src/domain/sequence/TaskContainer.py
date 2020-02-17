from .exceptions import WarningException


class TaskContainer:

    def __init__(self, sequence_event_emitter):
        self.__sequence_event_emitter = sequence_event_emitter
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    """
    Executes all the tasks, from the first one specified.

    :param first_task:
    :type str:
        The first task to execute. All the following tasks will also be executed.
    """
    def execute(self, first_task=None):
        tasks = self.__crop_to_first_task(first_task)

        for task in tasks:
            self.__sequence_event_emitter.send_task_started(task.name())
            self.__execute_task(task)

        self.__sequence_event_emitter.send_sequence_ended()

    """
    :param first_task:
    :type str:
        The first task to execute. All the following tasks will also be executed.
    """
    def __crop_to_first_task(self, first_task: str):
        if first_task is None:
            return self.tasks

        first_task_index = next(
            i for i, task in enumerate(self.tasks) if task.name() == first_task
        )

        return self.tasks[first_task_index:]

    """
    Executes a task and acts depending on the outcome / exceptions raised.

    :param task:
    :type Task:
        The task to execute.
    """
    def __execute_task(self, task):
        try:
            task.execute()
        except WarningException as exception:
            print(
                "Warning: '{}'. Passing on to the next task."
                .format(exception)
            )
            self.__sequence_event_emitter.send_task_warning(
                task.name(), str(exception)
            )
        except Exception as exception:
            self.__sequence_event_emitter.send_task_error(
                task.name(), str(exception)
            )
            raise exception
