from .exceptions import WarningException, RetryException


class TaskContainer:

    def __init__(self, sequence_event_emitter):
        self.__sequence_event_emitter = sequence_event_emitter
        self.__tasks = []

    def add_task(self, task):
        self.__tasks.append(task)

    def execute(self, first_task=None):
        tasks = self.__crop_to_first_task(first_task)

        for task in tasks:
            self.__sequence_event_emitter.send_task_started(task.name)
            self.__execute_task(task)

        self.__sequence_event_emitter.send_sequence_ended()

    def __crop_to_first_task(self, first_task):
        if first_task is None:
            return self.__tasks

        first_task_index = next(
            i for i, task in enumerate(self.__tasks) if task.name == first_task
        )[0]

        return self.__tasks[first_task_index:]

    def __execute_task(self, task):
        should_retry = True

        while should_retry:
            should_retry = False
            try:
                task.execute()
            except WarningException as exception:
                print(
                    "Warning: '{}'. Passing on to the next task."
                    .format(exception)
                )
                self.__sequence_event_emitter.send_task_warning(
                    task.name, str(exception)
                )
            except RetryException as exception:
                print(
                    "Retrying task '{}'. Message: '{}'"
                    .format(task.name, exception)
                )
                self.__sequence_event_emitter.send_task_retry(task.name)
                should_retry = True
            except Exception as exception:
                self.__sequence_event_emitter.send_task_error(
                    task.name, str(exception)
                )
                raise exception
