import pytest

from homework4.task01.magic_number import read_magic_number


@pytest.mark.parametrize("inp, result", [("2", True), ("3", False)])
def test_true_false_cases(file_with_true_and_false_value, result, inp):
    """Check the True and False cases"""
    assert read_magic_number(file_with_true_and_false_value) == result


def test_exception_case(file_with_exception_value):
    """Check case when file contain string that causes exception"""
    with pytest.raises(ValueError, match="It is not a magic number!"):
        read_magic_number(file_with_exception_value)


def test_existing_file_after_assert_error(exist_of_file):
    """
    Handle AssertionError to check that file do not
    exist after that
    """
    try:
        assert read_magic_number(exist_of_file)
    except AssertionError:
        print("Now lets do check of existing file")
