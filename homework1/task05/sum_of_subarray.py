"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    sum_subarray = sum(nums[:k])
    for i in range(len(nums) - (k - 1)):
        if sum_subarray < sum(nums[i : k + i]):
            sum_subarray = sum(nums[i : k + i])
    return sum_subarray