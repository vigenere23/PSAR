class RetryException(Exception):

    """
    Indicates that a task should be retried.
    This is handled by the Retryable decorator.
    """
    def __init__(self, task_name=None):
        if task_name:
            super().__init__("Retrying task '{}'".format(task_name))
        else:
            super().__init__("Retrying task")
