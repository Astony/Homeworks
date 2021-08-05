from typing import Any


class KeyValueStorage:
    """
        Class that has keys and values
    accessible as collection and as attributes.
    """

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        with open(file_path) as file:
            for pair in file:
                argument, value = pair.strip().split("=")
                try:
                    if argument.isidentifier() and argument not in dir(self):
                        self.__dict__[argument] = int(value)
                except ValueError:
                    self.__dict__[argument] = value

    def __getitem__(self, item: str) -> Any:
        if item in self.__dict__ or item in dir(self):
            return getattr(self, item)
        else:
            raise ValueError("No such key")
