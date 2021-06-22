from homework1.task05.sum_of_subarray import find_maximal_subarray_sum


def test_sum_of_subbarray():
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 4) == 21
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 1) == 7
