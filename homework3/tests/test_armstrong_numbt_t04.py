import pytest

from homework3.task04.armstrong_number import is_armstrong_number


@pytest.mark.parametrize(
    "test_input, result",
    [(153, True), (9, True), (27, False)],
)
def test_armstrong_number(test_input, result):
    """
    Check two cases with armstrong number
    and 1 case with not armstrong number
    """
    assert is_armstrong_number(153)
    assert is_armstrong_number(9)
    assert not is_armstrong_number(27)
