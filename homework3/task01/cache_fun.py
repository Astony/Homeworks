from typing import Callable

"""Parametrize cash decorator that 
stores the argument of n = size calls to a function
with the same argument"""


def cache(size: int) -> Callable:
    def real_cache(func: Callable) -> int:
        counter = {}
        storage = {}

        def wrapper(arg: int) -> int:
            if arg not in counter:
                counter[arg] = 0
                storage[arg] = func(arg)
                return storage[arg]
            else:
                counter[arg] += 1
                if counter[arg] == size:
                    del counter[arg]
                    result = storage[arg]
                    del storage[arg]
                return result

        return wrapper

    return real_cache


@cache(size=1)
def func(arg: int) -> int:
    return arg
