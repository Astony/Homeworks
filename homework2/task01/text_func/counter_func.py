from collections import Counter

"""Function return counter object with every char in text"""


def char_counter_func(file: str, encoding="utf8", errors="ignore"):
    counter = Counter()
    with open(file, encoding=encoding, errors=errors) as file:
        while char := file.read(1):
            counter[char] += 1
    return counter
