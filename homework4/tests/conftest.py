import os

import pytest


@pytest.fixture()
def create_right_file():
    test_file = open("test_file.txt", "w+")
    test_file.write("2")
    test_file.close()
    yield "test_file.txt"
    os.remove("test_file.txt")


@pytest.fixture()
def create_wrong_file():
    test_file = open("test_file.txt", "w+")
    test_file.write("3")
    test_file.close()
    yield "test_file.txt"
    os.remove("test_file.txt")


@pytest.fixture()
def create_exception_file():
    test_file = open("test_file.txt", "w+")
    test_file.write("1 2 3 4")
    test_file.close()
    yield "test_file.txt"
    os.remove("test_file.txt")


@pytest.fixture()
def exist_of_file():
    """Check the existence of file after failed test"""
    test_file = open("test_file.txt", "w+")
    test_file.write("3")
    test_file.close()
    yield "test_file.txt"
    os.remove("test_file.txt")
    assert not os.path.exists("test_file.txt")
