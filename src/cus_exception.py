class Error(Exception):
   """Base class for other exceptions"""
   pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        print(message + '\n')