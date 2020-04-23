class WarningException(Exception):

    """
    Indicates a non-critical error. This should be handled accordingly.
    """
    # TODO add message to logs
    def __init__(self, message):
        super().__init__(message)
