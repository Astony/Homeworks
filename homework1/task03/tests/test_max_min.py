from homework1.task03.max_min import find_maximum_and_minimum

file = open("empty_file.txt", "w")
file.write("1 2 3 4\n4 5 99 1\n2 4 0 1")
file.close()


def test_ideal_file():
    """Testing when ideal file with numbers in input"""
    assert find_maximum_and_minimum("empty_file.txt") == (0, 99)
