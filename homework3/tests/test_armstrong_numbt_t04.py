import pytest

from homework3.task04.armstrong_number import is_armstrong_number


@pytest.mark.parametrize(
    "test_input, result",
    [(153, True), (1634, True), (0, True), (23, False)],
)
def test_positive_numbers(test_input, result):
    """
    Check three cases with armstrong number
    and with not armstrong number
    """
    assert is_armstrong_number(test_input) == result


@pytest.mark.parametrize("test_input, result", [(-153, True), (-1634, False)])
def test_negative_numbers(test_input, result):
    """
    Check cases with numbers < 0
    """
    assert is_armstrong_number(test_input) == result


def test_non_integer_case():
    """Check ValueError case, when input value is not integer"""
    with pytest.raises(TypeError):
        is_armstrong_number("Non-integer value")
        print("Enter integer value")
