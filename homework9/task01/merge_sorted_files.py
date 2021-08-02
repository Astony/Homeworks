from itertools import zip_longest
from pathlib import Path
from typing import Generator, List


def numbers_generator_from_file(file_name: str) -> Generator[int, None, None]:
    """Generator that returns numbers from file one by one"""
    path = Path.cwd() / f"{file_name}"
    return (int(number) for number in path.read_text().split() if number != "\n")


def merge_sorted_files(file_list: List) -> Generator[int, None, None]:
    """Generator that merge two lists"""
    try:
        pairs_from_lists = zip_longest(
            numbers_generator_from_file(file_list[0]),
            numbers_generator_from_file(file_list[1]),
        )
        for pair in pairs_from_lists:
            for element in pair:
                if element:
                    yield element
    except ValueError:
        print("Files should have only integers")
