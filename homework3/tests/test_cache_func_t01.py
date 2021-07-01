from unittest.mock import Mock

from homework3.task01.cache_fun import cache, func

mock_func = Mock(func)
mock_decorator = cache(1)(mock_func)
"""func would be called with arg = 1"""
mock_decorator(1)
"""func would be called with arg = 2"""
mock_decorator(2)
"""the function will not be called, 
 the result of the function
  with this argument will be returned
   and then removed from the cache"""
mock_decorator(1)
"""same case"""
mock_decorator(2)
"""func would be called with arg = 1"""
mock_decorator(1)


def test_of_cache_func():
    assert mock_func.call_count == 3
