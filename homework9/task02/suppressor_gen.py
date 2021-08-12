from contextlib import contextmanager


@contextmanager
def suppressor_gen(error_type):
    """Generator that suppresses an exception that was given in argument"""
    exception = error_type
    try:
        yield
    except exception:
        return True
