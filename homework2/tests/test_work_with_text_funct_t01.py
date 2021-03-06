import pytest

from homework2.task01 import work_with_text

words_from_file = [
    "ÜBERSICHT",
    "Polykarp",
    "psycholo",
    "vorkommt",
    "Albdruck",
    "Kampfmit",
    "Zuflucht",
    "Komforts",
    "Zugzwang",
    "Rhythmus",
]
easy = ["mud", "ash", "boy", "cat", "cup", "jam", "rob", "lie", "pig", "beg"]

"""
For easy test there is easy_words.txt
# uniq of chars = {'b': 3, 'e': 5, 'g': 3,
 ' ': 12, 'a': 4, 's': 2, 'h': 1, 'j': 1,
  'm': 2, 'u': 2, 'd': 1, 'o': 3, 'c': 2,
   't': 1, 'l': 1, 'i': 3, 'y': 1, 'r': 1, 'p': 3}
# weight and words = [(5, 'mud'), (7, 'ash'), (7, 'boy'),
 (7, 'cat'), (7, 'cup'), (7, 'jam'), (7, 'rob'), (9, 'lie'),
  (9, 'pig'), (11, 'beg'), (11, 'ego'), (11, 'pie'), (11, 'sea')]
"""


@pytest.mark.parametrize(
    "test_input, result",
    [("homework2/data.txt", words_from_file), ("homework2/words.txt", easy)],
)
def test_get_longest_diverse_words(test_input, result):
    assert (
        work_with_text.get_longest_diverse_words(
            test_input, encoding="unicode-escape", errors="ignore"
        )
        == result
    )


@pytest.mark.parametrize(
    "test_input, result",
    [("homework2/data.txt", ")"), ("homework2/rarest_char.txt", "r")],
)
def test_get_rarest_char(test_input, result):
    assert (
        work_with_text.get_rarest_char(
            test_input, encoding="unicode-escape", errors="ignore"
        )
        == result
    )


@pytest.mark.parametrize(
    "test_input, result",
    [("homework2/data.txt", 5475), ("homework2/punctuation_marks.txt", 5)],
)
def test_count_punctuation_chars(test_input, result):
    assert (
        work_with_text.count_punc(
            test_input, encoding="unicode-escape", errors="ignore"
        )
        == result
    )


@pytest.mark.parametrize(
    "test_input, result",
    [("homework2/data.txt", 2972), ("homework2/non_ascii_chars.txt", 7)],
)
def test_count_non_ascii_chars(test_input, result):
    assert (
        work_with_text.non_ascii(test_input, encoding="unicode-escape", errors="ignore")
        == result
    )


@pytest.mark.parametrize(
    "test_input, result",
    [("homework2/data.txt", "ä"), ("homework2/non_ascii_chars.txt", "Ü")],
)
def test_get_most_common_non_ascii_char(test_input, result):
    assert (
        work_with_text.most_common_non_ascii(
            test_input, encoding="unicode-escape", errors="ignore"
        )
        == result
    )
