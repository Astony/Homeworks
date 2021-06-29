import pytest
from homework1.task02.check_fib import check_fibonacci


@pytest.mark.parametrize("test_input", [[0, 1, 1], [0, 1, 1, 2], [0, 1, 1, 2, 3]])
def test_right_sequences(test_input):
    """Testing RIGHT sequences of fibonacci"""
    assert check_fibonacci(test_input)


@pytest.mark.parametrize(
    "test_input", [[0, 1, 2], [0, 1, 1, 3], [0, 1, 1, 2, 1, 3, 4, 7], []]
)
def test_wrong_sequences(test_input):
    """Testing WRONG sequences of fibonacci and zero-len case"""
    assert not check_fibonacci(test_input)
