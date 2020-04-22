from abc import ABC
from typing import List
from src.domain.GlobalInfos import GlobalInfos
from src.domain.sequence.SequenceEventEmitter import SequenceEventEmitter
from src.domain.sequence.Task import Task
from src.domain.sequence.exceptions.WarningException import WarningException


class TaskContainer(ABC):

    def __init__(self, global_infos: GlobalInfos, sequence_event_emitter: SequenceEventEmitter):
        self.__global_infos = global_infos
        self.__sequence_event_emitter = sequence_event_emitter
        self.__tasks = []

    def _add_task(self, task):
        self.__tasks.append(task)

    def execute(self, first_task=None):
        """
        Executes all the tasks, from the first one specified.

        :param first_task: The first task to execute. All the following tasks will also be executed.
        """
        tasks = self.__crop_to_first_task(first_task)
        self._before_execution()

        task_names = [task.name() for task in tasks]
        self.__sequence_event_emitter.send_sequence_started(task_names)

        for task in tasks:
            self.__global_infos.wait_until_resumed()
            self.__sequence_event_emitter.send_task_started(task.name())
            self.__execute_task(task)
            self.__sequence_event_emitter.send_task_ended(task.name())

        self._after_execution()
        self.__sequence_event_emitter.send_sequence_ended()

    def _before_execution(self):
        """
        Execute before running any task

        """
        pass

    def _after_execution(self):
        """
        Execute after running any task

        """
        pass

    def __crop_to_first_task(self, first_task: str) -> List[Task]:
        """
        :param first_task: The first task to execute. All the following tasks will also be executed.
        :type first_task: str

        """
        if first_task is None:
            return self.__tasks

        first_task_index = next(
            i for i, task in enumerate(self.__tasks) if task.name() == first_task
        )

        return self.__tasks[first_task_index:]

    def __execute_task(self, task: Task):
        """
        Executes a task and acts depending on the outcome / exceptions raised.

        :param task: The task to execute.
        :type task: Task

        """
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
