import pytest
from homework9.task03.file_counter import universal_file_counter


def test_without_tokenizer_and_count_lines_into_file(
    create_directory_file_and_return_path,
):
    """Test that without passing tokenizer to function it returns the number of lines"""
    assert universal_file_counter(create_directory_file_and_return_path, "txt") == 8


def test_with_tokenizer_and_count_tokens(create_directory_file_and_return_path):
    """Test that if we pass tokenizer to function it returns the number of tokens"""
    assert (
        universal_file_counter(create_directory_file_and_return_path, "txt", str.split)
        == 6
    )


def test_with_non_existing_directory():
    """Test that it will raise error if file doesn't exist"""
    with pytest.raises(IOError, match="Can't find directory"):
        universal_file_counter("blablabla", "txt")
