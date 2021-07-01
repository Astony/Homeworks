import time

from homework3.task02.calc_func import slow_calculate, total_sum

a = [i for i in range(501)]

"""
Check time of calculation
"""


def test_of_calc_func():
    start_time = time.time()
    total_sum(a)
    assert time.time() - start_time < 60
