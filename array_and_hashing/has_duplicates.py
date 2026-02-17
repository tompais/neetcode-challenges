from typing import List


class Solution:
    def has_duplicate(self, nums: List[int]) -> bool:
        s = set(nums)

        return len(nums) != len(s)
