class TaskContainer:

    def __init__(self, sequence_event_emitter):
        self.__sequence_event_emitter = sequence_event_emitter
        self.__tasks = []

    def add_task(self, task):
        self.__tasks.append(task)

    def execute(self, first_task=None):
        tasks = self.__tasks
        if first_task is not None:
            first_task_index = next(
                i for i, task in enumerate(tasks) if task.name == first_task
            )[0]
            tasks = tasks[first_task_index:]

        for task in tasks:
            self.__sequence_event_emitter.send_task_started(task.name)
            try:
                task.execute()
            except Exception as exception:
                self.__sequence_event_emitter.send_error(
                    task.name, str(exception)
                )
