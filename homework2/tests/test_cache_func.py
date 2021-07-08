from unittest.mock import Mock

from homework2.task04.cash_func import cache, func

some = 100, 200


def test_of_cache_function():
    times_called = 0

    @cache
    def foo(a: int, b: int) -> int:
        nonlocal times_called
        times_called += 1
        return a * b

    foo(*some)
    foo(*some)
    assert times_called == 1
