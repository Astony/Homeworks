from collections import Counter
from typing import List, Tuple

"""
Function find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.
We may assume that the array is non-empty and the most common element
always exist in the array.
In requirements of the task does not say about the case when
the input list contains two numbers with the same repeatability. Therefore,
in the case of least common number,the smallest number will be chosen
"""


def major_and_minor_elem(list_elements: List[int]) -> Tuple[int, int]:
    counter_elements = Counter(sorted(list_elements, reverse=True))
    tup = counter_elements.most_common()[0][0], counter_elements.most_common()[-1][0]
    return tup
