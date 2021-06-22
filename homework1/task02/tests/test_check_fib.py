from homework1.task02.check_fib import check_fibonacci


def test_right_sequence():
    assert check_fibonacci([1, 1, 2, 3, 5, 8])
    assert check_fibonacci([3, 5, 8, 13, 21])
    assert check_fibonacci([1, 2, 3, 5, 8])


def test_wrong_sequence():
    assert not check_fibonacci([1, 1, 2, 3, 5, 7])
    assert not check_fibonacci([4, 5, 8, 13, 21])
    assert not check_fibonacci([7, 5, 3, 2, 1, 1])
