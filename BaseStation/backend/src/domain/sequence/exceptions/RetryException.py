class RetryException(Exception):

    """
    Indicates that a task should be retried.
    """
    def __init__(self, retries_left):
        super().__init__(
            "Retrying task : {} retry left"
            .format(retries_left)
        )
