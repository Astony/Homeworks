import unicodedata
from typing import Dict, List

"""
Function that return dict with each char from the text
and how many times the char repeated
"""


def char_dict(file: str, encoding="utf8", errors="ignore") -> Dict:
    with open(file, encoding=encoding, errors=errors) as file_input:
        char_dict = {}
        while char := file_input.read(1):
            if char != " " and char != "\n":
                if char not in char_dict:
                    char_dict[char] = 1
                else:
                    char_dict[char] += 1
            else:
                continue
    return char_dict
