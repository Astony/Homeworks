import os

import pytest
from homework4.task01.magic_number import read_magic_number


def test_right_case(create_right_file):
    """Check the positive case"""
    assert read_magic_number(create_right_file)


def test_wrong_case(create_wrong_file):
    """Check the negative case"""
    assert not read_magic_number(create_wrong_file)


def test_wrong_case_with_exception(create_exception_file):
    """Check the case with ValueError"""
    with pytest.raises(ValueError):
        read_magic_number(create_exception_file)


def test_existing_file_after_assert_error(exist_of_file):
    """
    Handle AssertionError to check that file do not
    exist after that
    """
    try:
        assert read_magic_number(exist_of_file)
    except AssertionError:
        print("Now lets do check of existing file")
