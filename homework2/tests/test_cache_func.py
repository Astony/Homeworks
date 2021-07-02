from homework2.task04.cash_func import cache, func
from mock import Mock

"""
Using mock we can get information about how many
times func was called
"""

mock_func = Mock(func)
mock_decorator = cache(mock_func)
some = 100, 200


def test_of_cache_function():
    mock_decorator(*some)
    mock_decorator(*some)
    mock_decorator(*some)
    assert mock_func.call_count == 1
