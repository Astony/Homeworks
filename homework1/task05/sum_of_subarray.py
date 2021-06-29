from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """Exclude case with zero or negative cases
    In this cases there is 0 on output"""
    if 0 < k <= len(nums) != 0:
        """Compare all next subarrays with the first"""
        sum_subarray = sum(nums[:k])
        for i in range(len(nums) - (k - 1)):
            if sum_subarray < sum(nums[i : k + i]):
                sum_subarray = sum(nums[i : k + i])
        return sum_subarray
    return 0
