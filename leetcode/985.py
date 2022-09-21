# 985. Sum of Even Numbers After Queries

from typing import List


class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        s = sum(a for a in A if a % 2 == 0)
        ans = []
        for val, idx in queries:
            if A[idx] % 2 == 0:
                s -= A[idx]
            A[idx] += val
            if A[idx] % 2 == 0:
                s += A[idx]
            ans.append(s)
        return ans
