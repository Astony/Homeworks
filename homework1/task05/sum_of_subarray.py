from typing import List


def find_maximal_subarray_sum(nums: List[int], sub_len: int) -> int:
    """Exclude case with zero or negative cases
    In this cases there is 0 on output"""
    if 0 < sub_len <= len(nums) != 0:
        """Compare all next subarrays with the first"""
        sum_subarray = sum(nums[:sub_len])
        for i in range(len(nums) - (sub_len - 1)):
            if sum_subarray < sum(nums[i : sub_len + i]):
                sum_subarray = sum(nums[i : sub_len + i])
        return sum_subarray
    return 0
