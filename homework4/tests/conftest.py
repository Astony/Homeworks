import os

import pytest

"""
All fixtures create test file.txt, write something into the file,
start tests with the file and then remove the file
 """
file = "test_file.txt"


@pytest.fixture()
def file_with_true_and_false_value(inp):
    """
    Create file and write into True or False cases
    """
    test_file = open(file, "w+")
    test_file.write(inp)
    test_file.close()
    yield file
    os.remove(file)


@pytest.fixture()
def file_with_exception_value():
    """
    Fixture for exception case
    """
    test_file = open(file, "w+")
    test_file.write("1 2 3 5")
    test_file.close()
    yield file
    os.remove(file)


@pytest.fixture()
def exist_of_file():
    """Check the existence of file after failed test"""
    test_file = open(file, "w+")
    test_file.write("3")
    test_file.close()
    yield file
    os.remove(file)
    assert not os.path.exists(file)
