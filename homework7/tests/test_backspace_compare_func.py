import pytest

from homework7.task02.backspace_compare import backspace_compare


@pytest.mark.parametrize(
    "str1, str2, result",
    [
        ("ab    c", "   ad c", True),
        ("a       c", "   a   c", True),
        ("ab    c", "   r", False),
    ],
)
def test_positive_and_negative_cases(str1, str2, result):
    assert backspace_compare(str1, str2) == result
