class TaskContainer:

    def __init__(self, socketio):
        self.__socketio = socketio
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
            self.__socketio.emit(
                'task_started', task.name, namespace='/sequence'
            )
            try:
                task.execute()
            except Exception as exception:
                self.__socketio.emit(
                    'error',
                    {'task': task.name, 'message': str(exception)},
                    namespace='/sequence'
                )
