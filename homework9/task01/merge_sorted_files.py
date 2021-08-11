from contextlib import ExitStack
from itertools import chain, zip_longest
from typing import Generator, List


def merge_sorted_files(file_list: List) -> Generator[int, None, None]:
    """Generator that merge two lists"""
    with ExitStack() as stack:
        files = [stack.enter_context(open(fname)) for fname in file_list]
        file1, file2 = files[0].readlines(), files[1].readlines()
        try:
            for element in (
                element for element in chain(*zip_longest(file1, file2)) if element
            ):
                yield int(element.strip())
        except ValueError:
            print("Files should have only integers")
