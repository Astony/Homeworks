import string
from typing import Tuple

"""
The function remove all punctuation marks and numbers
from input string, count every char and then give
dict with counted chars and reshaped text on the output
"""


def dict_and_text(text: str) -> Tuple:
    count_dict = {}
    for char in text:
        if (
            char in string.punctuation
            or ord(char) in [171, 187, 2014, 2013]
            or char.isdigit()
        ):
            text = text.replace(char, "")
        elif char not in count_dict.keys():
            count_dict[char] = 1
        else:
            count_dict[char] += 1
    return count_dict, text
