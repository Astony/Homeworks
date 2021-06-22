from homework1.task03.max_min import find_maximum_and_minimum


def test_ideal_file():
    """Testing when ideal file with numbers in input"""
    assert find_maximum_and_minimum("numbers.txt") == (0, 99)
