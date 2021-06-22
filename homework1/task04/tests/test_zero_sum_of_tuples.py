from homework1.task04.zero_sum_of_tuples import check_sum_of_four


def test_simple_check():
    """Testing when the dimension of our tuples is 1"""
    assert check_sum_of_four([1], [-1], [1], [-1]) == 1


def test_harder_check():
    """Testing when the dimension of our tuples is 2
    in this case there are six combinations of numbers:
    [1,-1,1,-1],
    [1,-1,30,-30],
    [1,-30,30,-1],
    [30,-1,1,-30],
    [30,-30,1,-1],
    [30,-30,30,-30]"""

    assert check_sum_of_four([1, 30], [-1, -30], [1, 30], [-1, -30]) == 6
