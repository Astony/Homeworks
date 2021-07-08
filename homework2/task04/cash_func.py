from functools import lru_cache
from typing import Callable

"""                                             
Keep all arguments and results in storage dict  
and return data from depending on the input args
"""

cache = lru_cache()


@cache
def func(a: int, b: int) -> int:
    return (a * b) * 2
