import os
from pathlib import Path

import pytest


@pytest.fixture()
def create_files(strings):
    """
    Fixture that creates two txt files, writes some text into them,
    start tests and removes files after that.
    """
    with open("test1.txt", "w") as file1:
        file1.write(strings[0])
    with open("test2.txt", "w") as file2:
        file2.write(strings[1])
    yield "test1.txt", "test2.txt"
    os.remove("test1.txt")
    os.remove("test2.txt")


@pytest.fixture()
def create_directory_file_and_return_path():
    """
    Fixture that creates new directory, some files into that directory,
    writes some text into files, starts tests and removes
    files and directories after that.
    """
    new_directory = Path("temp/")
    new_directory.mkdir(parents=True, exist_ok=True)
    file_paths = []
    for i in range(1, 3):
        file_name = f"file{i}.txt"
        filepath = new_directory / file_name
        filepath.write_text("aaa\nbbb\nccc\n")
        file_paths.append(filepath)
    yield new_directory
    for filepath in file_paths:
        filepath.unlink()
    new_directory.rmdir()
