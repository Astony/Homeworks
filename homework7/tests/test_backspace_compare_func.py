import pytest

from homework7.task02.backspace_compare import backspace_compare


@pytest.mark.parametrize(
    "str1, str2, result",
    [
        ("ab    c", "   ad c", True),
        ("a       c", "   a   c", True),
        ("ab    c", "   r", False),
        ("     ", " ", True),
        ("equal", "equal", True),
    ],
)
def test_positive_and_negative_cases(str1, str2, result):
    """
    Check positive and negative cases
    and also cases with backspace char string
    and string without backspaces
    """
    assert backspace_compare(str1, str2) == result
