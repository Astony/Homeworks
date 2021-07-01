from typing import Callable


def func(a, b):
    return (a * b) * 2


"""
Keep all arguments and results in storage dict
and return data from depending on the input args
"""


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args, **kwargs):
        if not storage.get(args):
            func_value = func(*args, **kwargs)
            storage[args] = func_value
            return func_value
        else:
            return storage[args]

    return wrapper
