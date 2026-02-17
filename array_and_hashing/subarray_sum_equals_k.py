from typing import List


class Solution:
    def subarray_sum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0: 1}
        current_sum = 0
        count = 0
        for num in nums:
            current_sum += num
            count += prefix_sums.get(current_sum - k, 0)
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
        return count
