from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        result = -1

        while left <= right and result == -1:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result
