def shape_string(string: str) -> str:
    """
    Function that modifies string by deleting backspace
            chars and 1 char before backspace.
    """
    shaped_string = ""
    while True:
        index = string.find(" ")
        if index == 0:
            string = string[1:]
        elif index == -1:
            shaped_string += string
            return shaped_string
        else:
            shaped_string += string[: index - 1]
            string = string[index + 1 :]


def backspace_compare(string1: str, string2: str) -> bool:
    """Function that compare strings that contain backspaces"""
    return shape_string(string1) == shape_string(string2)
