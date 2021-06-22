from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open(file_name, "r") as inp:
        line1 = inp.readline().strip().split()
        min_int = min(line1)
        max_int = max(line1)
        for lines in inp:
            line = lines.strip().split()
            if min_int > min(line):
                min_int = min(line)
            elif max_int < max(line):
                max_int = max(line)
        return int(min_int), int(max_int)
