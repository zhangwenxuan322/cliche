# 1770. Maximum Score from Performing Multiplication Operations


from functools import lru_cache
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        lr = [0]*(len(multipliers)+1)
        for l, m in enumerate(reversed(multipliers), start=len(nums)-len(multipliers)):
            lr = [max(m*nums[i]+lr[i+1], m*nums[i+l]+lr[i])
                  for i, n in enumerate(lr[:-1])]
        return max(lr)
