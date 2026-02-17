from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        result = []
        i = 0
        found = False
        while i < len(nums) and not found:
            num = nums[i]
            complement = target - num
            if complement in num_to_index:
                result = [num_to_index[complement], i]
                found = True
            else:
                num_to_index[num] = i
            i += 1
        return result
