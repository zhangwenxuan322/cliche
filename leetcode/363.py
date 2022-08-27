# 363. Max Sum of Rectangle No Larger Than K


import bisect
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        res = - 2**31
        for ii in range(m):
            sums = [0] * n
            for i in range(ii, m):
                sorted_ps, ps = [], 0
                for j in range(n):
                    sums[j] += matrix[i][j]
                    ps += sums[j]
                    if ps <= k:
                        res = max(res, ps)
                    index = bisect.bisect_left(sorted_ps, ps - k)
                    if index < len(sorted_ps):
                        res = max(res, ps - sorted_ps[index])
                    bisect.insort(sorted_ps, ps)
        return res
