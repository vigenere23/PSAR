class RetriesExceededException(Exception):

    """
    Indicates that the number of permitted retries has been exceeded.
    """
    def __init__(self, number_of_retries):
        super().__init__(
            "Number of retries ({}) exceeded"
            .format(number_of_retries)
        )
