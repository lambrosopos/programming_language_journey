"""
Runtime: 116 ms, faster than 91.24%
Memory Usage: 14.7 MB, less than 8.49%
"""

from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[idx]] for idx in range(len(nums))]
