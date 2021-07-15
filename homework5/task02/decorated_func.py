from functools import reduce, update_wrapper
from typing import Any, Callable, ClassVar, Tuple


class Saver:
    """
    Class Saver save original func in the separate attribute and also
    use method update_wrapper to wrapper function and save all attributes of
    original function
    """

    def __init__(self, func: Callable) -> None:
        self.original_func = func

    def __call__(self, *args: Any, **kwargs: Any) -> ClassVar:
        return update_wrapper(self, self.original_func)


def print_result(func: Callable) -> Callable:
    @Saver(func)
    def wrapper(*args: Any, **kwargs: Any) -> Callable:
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


@print_result
def custom_sum(*args: Tuple) -> Tuple:
    """This function can sum any objects which have __add___"""
    return reduce(lambda x, y: x + y, args)
