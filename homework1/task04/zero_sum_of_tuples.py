from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """Dictionary, where keys - sums of elements of lists a and b
    and values - numbers of their repetitions"""
    sums_dict = {}
    for i in a:
        for j in b:
            if i + j not in sums_dict:
                sums_dict[i + j] = 1
            else:
                sums_dict[i + j] += 1
    counter = 0
    """Search how many times sums of elements for c and d
    gives a zero with sums elements with a and b"""
    for k in c:
        for l in d:
            if -1 * (k + l) in sums_dict:
                counter += sums_dict[-1 * (k + l)]
    return counter
