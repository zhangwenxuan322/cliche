# 377. Combination Sum IV

from functools import lru_cache
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dp(remain):
            if remain == 0:
                return 1
            partialRes = 0
            for num in nums:
                if remain - num < 0:
                    continue
                partialRes += dp(remain - num)
            return partialRes
        return dp(target)
