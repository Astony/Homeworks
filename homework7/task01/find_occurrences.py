from typing import Any


def find_occurrences(tree: dict, required_element: Any) -> int:
    counter = 0
    if tree == required_element:
        counter += 1
    elif isinstance(tree, (list, set, tuple)):
        for element in tree:
            counter += find_occurrences(element, required_element)
    elif isinstance(tree, dict):
        for key, value in tree.items():
            if value == required_element:
                counter += 1
            else:
                counter += find_occurrences(value, required_element)
    return counter
