import os

import pytest

file = "test_file.txt"


"""
All fixtures create file, write some rows inside, 
  send file in tests func and then delete file
"""


@pytest.fixture()
def create_file_with_valid_attr_val():
    with open(file, "w+") as test_file:
        test_file.write("name=kek\nlast_name=2")
    yield file
    os.remove(file)


@pytest.fixture()
def create_file_with_invalid_attr_val():
    with open(file, "w+") as test_file:
        test_file.write("1=invalid_attribute")
    yield file
    os.remove(file)


@pytest.fixture()
def create_file_with_clash_attr():
    with open(file, "w+") as test_file:
        test_file.write("__class__=boo")
    yield file
    os.remove(file)
