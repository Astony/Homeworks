from unittest.mock import Mock

import pytest

from homework3.task01.cache_fun import cache, func

some = 100, 200
uncacheable_argument = [1, 2, 3]


def test_of_cache_function():
    times_called = 0

    @cache(size=1)
    def foo(a: int, b: int) -> int:
        nonlocal times_called
        times_called += 1
        return a * b

    foo(*some)
    foo(*some)
    foo(*some)
    assert times_called == 2


def test_of_uncacheable_argument():
    with pytest.raises(TypeError):
        func([1, 2, 3])
        print("Enter cacheable argument")
