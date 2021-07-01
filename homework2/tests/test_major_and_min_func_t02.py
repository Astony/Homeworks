import pytest

from homework2.task02.major_and_min_func import major_and_minor_elem


@pytest.mark.parametrize(
    "test_input, result",
    [([1, 1, 1, 1, 1, 5, 6], (1, 5)), ([1, 1, 1, 1, 1, 5, 5], (1, 5))],
)
def test_of_positive_case(test_input, result):
    assert major_and_minor_elem(test_input) == result


@pytest.mark.parametrize(
    "test_input, result",
    [
        ([1, 1, 1, 1, 1], (1, 1)),
    ],
)
def test_of_equal_numbers_case(test_input, result):
    assert major_and_minor_elem(test_input) == result
