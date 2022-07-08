# 1473. Paint House III

from typing import List


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = {}

        def dfs(i, t, p):
            key = (i, t, p)

            if i == len(houses) or t < 0 or m - i < t:
                return 0 if t == 0 and i == len(houses) else float('inf')

            if key not in dp:
                if houses[i] == 0:
                    dp[key] = min(dfs(i + 1, t - (nc != p), nc) +
                                  cost[i][nc - 1] for nc in range(1, n + 1))
                else:
                    dp[key] = dfs(i + 1, t - (houses[i] != p), houses[i])

            return dp[key]

        ret = dfs(0, target, -1)
        return ret if ret < float('inf') else -1
