from itertools import product
from typing import Any, List

"""
In first we create all of available combinations and
then thi filter combination if it numbers not in this place
"""


def combinations(list_of_lists: List[Any]) -> List[List]:
    if all(map(lambda x: len(x) == len(list_of_lists), list_of_lists)):
        combo_out = []
        combo_in = list(product(*list_of_lists))
        for i in combo_in:
            combo_out.append(list(i))
        return combo_out
    else:
        raise ValueError("Invalid input argument, check dimensions")
