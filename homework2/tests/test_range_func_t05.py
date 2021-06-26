from homework2.task05.range_func import custom_range

integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
char = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def test_of_range_func_char():
    assert custom_range(char, "g") == ["a", "b", "c", "d", "e", "f"]
    assert custom_range(char, "g", "p") == ["g", "h", "i", "j", "k", "l", "m", "n", "o"]
    assert custom_range(char, "p", "g", -2) == ["p", "n", "l", "j", "h"]


def test_of_range_func_integers():
    assert custom_range(integers, 5) == [0, 1, 2, 3, 4]
    assert custom_range(integers, 1, 9) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert custom_range(integers, 7, 1, -1) == [7, 6, 5, 4, 3, 2]
