from homework2.task04.cash_func import cache, func

cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)


def test_of_cache_function():
    assert val_1 is val_2
