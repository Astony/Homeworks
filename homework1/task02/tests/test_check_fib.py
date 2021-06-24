from homework1.task02.check_fib import check_fibonacci


def test_right_sequence():
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8, 13])


def test_wrong_sequence():
    assert not check_fibonacci([0, 1, 1, 2, 3, 5, 7])
