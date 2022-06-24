# 1354. Construct Target Array With Multiple Sums
import heapq
from typing import List


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        A = [-a for a in target]
        heapq.heapify(A)
        while True:
            a = -heapq.heappop(A)
            total -= a
            if a == 1 or total == 1: return True
            if a < total or total == 0 or a % total == 0:
                return False
            a %= total
            total += a
            heapq.heappush(A, -a)
