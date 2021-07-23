from typing import Any, List


def read_valid_attributes_and_values(path: str) -> List:
    """Function that reads and checks attributes and values from file."""
    valid_attributes_and_values = []
    with open(path, "r") as file:
        attr_and_val = file.read().split()
    for pair in attr_and_val:
        attribute, value = pair.split("=")
        if attribute.isdigit():
            raise ValueError("Invalid name for attribute")
        elif attribute in dir(KeyValueStorage):
            continue
        elif value.isdigit():
            value = int(value)
        valid_attributes_and_values.append((attribute, value))
    return valid_attributes_and_values


class KeyValueStorage:
    """
        Class that has keys and values
    accessible as collection and as attributes.
    """

    def __init__(self, path: str) -> None:
        valid_attributes_and_values = read_valid_attributes_and_values(path)
        for attribute, value in valid_attributes_and_values:
            setattr(self, attribute, value)

    def __getitem__(self, attribute: str) -> Any:
        if attribute in dir(self):
            return getattr(self, attribute)
        return self.__dict__[attribute]
