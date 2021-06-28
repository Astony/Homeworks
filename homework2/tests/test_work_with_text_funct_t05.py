from homework2.task01.work_with_text import (count_non_ascii_chars,
                                             count_punctuation_chars,
                                             get_longest_diverse_words,
                                             get_most_common_non_ascii_char,
                                             get_rarest_char)


def test_get_longest_diverse_words():
    assert get_longest_diverse_words("data.txt") == [
        "ÜBERSICHT",
        "Symbol",
        "vollzo",
        "klopft",
        "Sowohl",
        "vollkom",
        "Ablauf",
        "obwohl",
        "Scylla",
        "Vakuum",
    ]


def test_get_rarest_char():
    assert get_rarest_char("data.txt") == "›"


def test_count_punctuation_chars():
    assert count_punctuation_chars("data.txt") == 5392


def test_count_non_ascii_chars():
    assert count_non_ascii_chars("data.txt") == 2972


def test_get_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char("data.txt") == "ä"
