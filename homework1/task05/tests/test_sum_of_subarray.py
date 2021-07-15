import pytest

from homework1.task05.sum_of_subarray import find_maximal_subarray_sum


@pytest.mark.parametrize(
    "array, sub_len, expected",
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([1, 3, -1, -3, 5, 3, 6, 7], 4, 21),
        ([1, 3, -1, -3, 5, 3, 6, 7], 1, 7),
    ],
)
def test_sum_of_subbarray_positive_cases(array, sub_len, expected):
    assert find_maximal_subarray_sum(array, sub_len) == expected


"""Test with cases zero-len input list/step>len(list)/negative step"""


@pytest.mark.parametrize("array, sub_len", [([], 3), ([1, 3, -1], 4), ([1, 3, -1], -1)])
def test_sum_of_subbarray_exception_cases(array, sub_len):
    with pytest.raises(ValueError):
        assert find_maximal_subarray_sum(array, sub_len)
