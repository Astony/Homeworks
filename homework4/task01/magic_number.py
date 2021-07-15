"""
Function return True or False, if type of line in file
is int, otherwise if it has another type, func return ValueError
"""


def read_magic_number(path: str) -> bool:
    with open(path, "r") as file:
        try:
            line = file.readline().strip()
            return 1 <= float(line) < 3
        except Exception as err:
            raise ValueError("It is not a magic number!") from err
