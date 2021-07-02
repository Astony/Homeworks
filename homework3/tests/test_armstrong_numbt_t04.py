import pytest

from homework3.task04.armstrong_number import is_armstrong_number


@pytest.mark.parametrize(
    "test_input, result",
    [(153, True), (9, True), (0, True), (23, False)],
)
def test_armstrong_number(test_input, result):
    """
    Check three cases with armstrong number
    and with not armstrong number
    """
    assert is_armstrong_number(test_input) == result
