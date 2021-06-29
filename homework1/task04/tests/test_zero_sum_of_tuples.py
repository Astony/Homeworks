import pytest

from homework1.task04.zero_sum_of_tuples import check_sum_of_four

"""Testing when the dimension of our tuples is 1"""
lst1 = [[1], [-1], [1], [-1]]
"""Testing when the dimension of our tuples is 2
in this case there are six combinations of numbers:
[1,-1,1,-1],
[1,-1,30,-30],
[1,-30,30,-1],
[30,-1,1,-30],
[30,-30,1,-1],
[30,-30,30,-30]"""
lst2 = [[1, 30], [-1, -30], [1, 30], [-1, -30]]


@pytest.mark.parametrize("test_input, expected", [(lst1, 1), (lst2, 6)])
def test_sums_of_fours(test_input, expected):
    assert check_sum_of_four(*test_input) == expected
