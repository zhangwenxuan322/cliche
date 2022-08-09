# 823. Binary Trees With Factors


from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 1000 * 1000 * 1000 + 7
        arr = sorted(arr)
        dp = {a: 1 for a in arr}

        for i, a in enumerate(arr):
            for j in range(i):
                b, c = arr[j], a//arr[j]
                if c < b:
                    break
                if a % b != 0 or c not in dp:
                    continue
                add = dp[b] * dp[c]
                dp[a] += add if b == c else 2 * add
            dp[a] = dp[a] % mod
        return sum(dp.values()) % mod
