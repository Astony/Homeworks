from homework2.task01 import work_with_text


def test_get_longest_diverse_words():
    assert work_with_text.get_longest_diverse_words("data.txt") == [
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
    assert work_with_text.get_rarest_char("data.txt") == "›"


def test_count_punctuation_chars():
    assert work_with_text.count_punctuation_chars("data.txt") == 5392


def test_count_non_ascii_chars():
    assert work_with_text.count_non_ascii_chars("data.txt") == 2972


def test_get_most_common_non_ascii_char():
    assert work_with_text.get_most_common_non_ascii_char("data.txt") == "ä"
