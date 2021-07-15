from typing import Callable

"""Parametrize cash decorator that 
stores the argument of n = size calls to a function
with the same argument"""


def cache(size: int) -> Callable:
    def real_cache(func: Callable):
        storage = {}

        def wrapper(*args, **kwargs):
            if (not storage) or (storage and storage[args][1] >= size):
                """Now we store both result of function and number of calls it"""
                storage[args] = [func(*args, **kwargs), 0]
            else:
                storage[args][1] += 1
            return storage[args][0]

        return wrapper

    return real_cache


@cache(size=1)
def func(a, b):
    return a * b
