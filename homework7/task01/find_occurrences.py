from typing import Any


def find_occurrences(item: dict, required_element: Any) -> int:
    """
    The function gives access for all values in nested structure and allows
                count the quantity of the required element.
    """
    counter = 0
    if item == required_element:
        counter += 1
    elif isinstance(item, (list, set, tuple)):
        for element in item:
            counter += find_occurrences(element, required_element)
    elif isinstance(item, dict):
        for key, value in item.items():
            if value == required_element:
                counter += 1
            else:
                counter += find_occurrences(value, required_element)
    return counter
