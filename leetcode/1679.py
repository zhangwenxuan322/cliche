# 1679. Max Number of K-Sum Pairs
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        ans = 0
        while l < r:
            if nums[r] + nums[l] == k:
                ans += 1
                l += 1
                r -= 1
            elif nums[r] + nums[l] > k:
                r -= 1
            else:
                l += 1

        return ans
