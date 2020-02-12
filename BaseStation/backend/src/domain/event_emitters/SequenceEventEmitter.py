class SequenceEventEmitter:

    def send_task_started(self, task_name):
        raise NotImplementedError()

    def send_sequence_ended(self):
        raise NotImplementedError()

    def send_error(self, task_name, message):
        raise NotImplementedError()
