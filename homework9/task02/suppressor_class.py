class Suppressor:
    """Class that suppresses an exception that was given in argument"""

    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        return exc_type is self.exception
