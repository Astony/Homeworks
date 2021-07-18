"""
Function return True or False, if type of line in file
is int, otherwise if it has another type, func return ValueError
"""


def line_reader_func(path: str) -> str:
    with open(path, "r") as file:
        line = file.readline().strip()
    return line


def read_magic_number(path: str) -> bool:
    line = line_reader_func(path)
    try:
        return 1 <= float(line) < 3
    except Exception as err:
        raise ValueError("It is not a magic number!") from err
