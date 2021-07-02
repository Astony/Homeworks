import unicodedata
from typing import Dict, List

"""Generator that return list of words from file"""


def words_list(file: str, encoding="utf8", errors="ignore") -> List[str]:
    with open(file, encoding=encoding, errors=errors) as file_input:
        buffer = []
        while char := file_input.read(1):
            char_type = unicodedata.category(char)
            if char_type.startswith("L"):
                buffer += char
            elif char_type != char_type.startswith("L"):
                if buffer:
                    yield "".join(buffer)
                    buffer = []
