import unicodedata
from typing import Dict, List

"""
Function that return dict with each letter from the text
and how many times the letter repeated
"""


def letter_dict(file: str, encoding="utf8", errors="ignore") -> Dict:
    with open(file, encoding=encoding, errors=errors) as file_input:
        dict_char = {}
        while char := file_input.read(1):
            if unicodedata.category(char).startswith("L"):
                if char not in dict_char:
                    dict_char[char] = 1
                else:
                    dict_char[char] += 1
        return dict_char
