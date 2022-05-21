# 322. Coin Change
import math
from functools import lru_cache
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dp(i, amount):
            if amount == 0:
                return 0
            if i == -1:
                return math.inf

            ans = dp(i - 1, amount)  # Skip ith coin
            if amount >= coins[i]:  # Used ith coin
                ans = min(ans, dp(i, amount - coins[i]) + 1)
            return ans

        n = len(coins)
        ans = dp(n - 1, amount)
        return ans if ans != math.inf else -1
