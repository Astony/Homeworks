"""
Function return True or False, if type of line in file
is int, otherwise if it has another type, func return ValueError
"""


def read_magic_number(path: str) -> bool:
    with open(path, "r") as file:
        line = file.readline().strip()
        if line.isdigit():
            if 1 <= int(line) < 3:
                return True
            else:
                return False
        else:
            raise ValueError("It is not a magic number!")
