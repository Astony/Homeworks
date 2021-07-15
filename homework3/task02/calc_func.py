import hashlib
import random
import struct
import time
from multiprocessing import Pool
from typing import List


def slow_calculate(value: int) -> int:
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


"""
Divide the calculations into several streams
Create new list and find sum
"""


def total_sum(numbers: List) -> int:
    with Pool(32) as p_object:
        changed_numbs = p_object.map(slow_calculate, numbers)
        result = sum(changed_numbs)
        return result
