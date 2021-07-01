"""In requirements of the task does not say about the case when
the input list contains two numbers with the same repeatability. Therefore,
in the case of least common number,the smallest number will be chosen """
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    if len(set(inp)) > 1:
        elements_quanity = {elem: inp.count(elem) for elem in set(inp)}
        for element, quanity in elements_quanity.items():
            if quanity > len(inp) // 2:
                most_common = element
                elements_quanity.pop(element)
                break
        for element, quanity in elements_quanity.items():
            if quanity == min(elements_quanity.values()) and element == min(
                elements_quanity.keys()
            ):
                least_common = element
                break
        return most_common, least_common
    else:
        return inp[0], inp[0]
