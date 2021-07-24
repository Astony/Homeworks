from functools import reduce, update_wrapper
from typing import Any, Callable, ClassVar, Tuple


def save_orig_func_info(donor_func):
    def decorator(recipient_func):
        recipient_func.__doc__ = donor_func.__doc__
        recipient_func.__name__ = donor_func.__name__
        recipient_func.orig_func = donor_func
        return recipient_func
    return decorator


def print_result(func: Callable) -> Callable:
    @save_orig_func_info(func)
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
