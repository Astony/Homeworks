import pytest

from homework9.task01.merge_sorted_files import merge_sorted_files

valid_text = ["1\n3\n5\n13", "2\n4\n6"]
invalid_text = ["a\n2", "1\n2"]


@pytest.mark.parametrize("strings", [valid_text])
def test_with_different_number_of_lines_in_file(create_files):
    """
    Test with case of valid files with different number of integers
    into them
    """
    list1, list2 = create_files
    assert list(merge_sorted_files([list1, list2])) == [1, 2, 3, 4, 5, 6, 13]


@pytest.mark.parametrize("strings", [valid_text])
def test_that_func_returns_iter_obj(create_files):
    """
    Test that returning value corresponds to protocol of iterator.
    """
    file1, file2 = create_files
    iterator = merge_sorted_files([file1, file2])
    for index in range(7):
        next(iterator)
    with pytest.raises(StopIteration):
        next(iterator)


@pytest.mark.parametrize("strings", [invalid_text])
def test_with_invalid_content_in_files(create_files, capsys):
    """
    Test with case of invalid files
    """
    list1, list2 = create_files
    list(merge_sorted_files([list1, list2]))
    assert capsys.readouterr().out == "Files should have only integers\n"
