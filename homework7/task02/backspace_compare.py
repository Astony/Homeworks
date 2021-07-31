def shape_string(string: str) -> str:
    """Generator that yields shaped string"""
    backspace_counter = 0
    for char in reversed(string):
        if char == "#":
            backspace_counter += 1
            continue
        elif backspace_counter != 0 and char != "#":
            backspace_counter = 0
            continue
        yield char


def backspace_compare(string1: str, string2: str) -> bool:
    """Function that compare strings that contain backspaces"""
    for elem1, elem2 in zip(shape_string(string1), shape_string(string2)):
        if elem1 != elem2:
            return False
    return True
