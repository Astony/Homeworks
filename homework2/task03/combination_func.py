import itertools
from typing import Any, List

"""
In first we create all of available combinations and
then thi filter combination if it numbers not in theis place
"""


def combinations(list_of_lists: List[Any]) -> List[List]:
    all_elements = list(itertools.chain(*list_of_lists))
    combos = list(itertools.combinations(all_elements, len(list_of_lists)))
    iterator = 0
    while iterator != len(list_of_lists):
        sorted_list_of_combinations = [
            i for i in combos if i[iterator] in list_of_lists[iterator]
        ]
        combos = sorted_list_of_combinations[:]
        iterator += 1
    return list(map(list, sorted_list_of_combinations))
