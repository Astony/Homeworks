"""In requirements of the task does not say about the case when
the input list contains two numbers with the same repeatability. Therefore,
in the case of least common number,the smallest number will be chosen """
from typing import List, Tuple

"""
Function find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

"""


def major_and_minor_elem(list_elements: List) -> Tuple[int, int]:
    if len(set(list_elements)) > 1:
        elements_quantity = {
            elem: list_elements.count(elem) for elem in set(list_elements)
        }
        for element, quantity in elements_quantity.items():
            if quantity > len(list_elements) // 2:
                most_common = element
                elements_quantity.pop(element)
                break
        for element, quantity in elements_quantity.items():
            if quantity == min(elements_quantity.values()) and element == min(
                elements_quantity.keys()
            ):
                least_common = element
                break
        return most_common, least_common
    else:
        return list_elements[0], list_elements[0]
