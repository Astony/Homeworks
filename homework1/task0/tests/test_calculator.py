import pytest

from homework1.task0.calculator.calc import check_power_of_2


@pytest.mark.parametrize("test_input", [65536, 2])
def test_positive_cases(test_input):
    """Check the numbers that are powers of two"""
    assert check_power_of_2(test_input)


@pytest.mark.parametrize("test_input", [12, 3])
def test_negative_cases(test_input):
    """Check the numbers that are NOT powers of two"""
    assert not check_power_of_2(test_input)


def test_zero_case():
    """Check the case with zero input"""
    assert not check_power_of_2(0)
