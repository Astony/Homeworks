from typing import List, Tuple

"""Reading integers from file function"""


def read_file(file_name: str) -> List[int]:
    numbers_list = []
    with open(file_name, "r") as inp:
        for line in inp:
            numbers_list.append(int(line))
    return numbers_list


"""Search of max and min integers from list"""


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    list_of_numbers = read_file(file_name)
    min_int = min(list_of_numbers)
    max_int = max(list_of_numbers)
    return min_int, max_int
