import pytest

from homework2.task05.range_func import custom_range

integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

"""Testing 3 cases with 1,2 and 3 arguments"""


@pytest.mark.parametrize(
    "collection, args, result",
    [
        (integers, [5], [0, 1, 2, 3, 4]),
        (integers, [1, 9], [1, 2, 3, 4, 5, 6, 7, 8]),
        (integers, [7, 1, -1], [7, 6, 5, 4, 3, 2]),
    ],
)
def test_of_range_func_integers(collection, args, result):
    assert custom_range(collection, *args) == result
