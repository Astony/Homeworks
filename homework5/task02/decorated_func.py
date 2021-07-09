import functools


class Saver:
    """
    Class Saver save original func in the separate attribute and also
    use method update_wrapper to wrapper function and save all attributes of
    original function
    """

    def __init__(self, func):
        self.original_func = func

    def __call__(self, *args, **kwargs):
        return functools.update_wrapper(self, self.original_func)


def print_result(func):
    @Saver(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)
