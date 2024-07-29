class CustomException(BaseException):
    """
    This class manages custom exceptions.
    """

    def __init__(self, message):
        super().__init__(message)
        self.message = message
