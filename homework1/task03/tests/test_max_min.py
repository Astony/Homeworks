import pytest
from homework1.task03.max_min import find_maximum_and_minimum


@pytest.mark.parametrize(
    "file_name, result",
    [("homework1/numbs.txt", (-100, 100)), ("homework1/zeros.txt", (0, 0))],
)
def test_ideal_file_and_file_with_zeros(file_name, result):
    """Testing when ideal file with different numbers in input
    and file with equal numbers"""
    assert find_maximum_and_minimum(file_name) == result
