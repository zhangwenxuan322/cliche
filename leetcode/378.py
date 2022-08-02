# 378. Kth Smallest Element in a Sorted Matrix

from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        lo = matrix[0][0]
        hi = matrix[-1][-1]

        def valid(x):
            count = 0
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] <= x:
                        count += 1
            return count < k

        while lo < hi:
            mid = lo + hi >> 1

            if valid(mid):
                lo = mid + 1
            else:
                hi = mid

        return lo
