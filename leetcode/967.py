# 967. Numbers With Same Consecutive Differences

from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []

        def backtrack(tempRes):
            nonlocal res
            if len(tempRes) == n:

                s = [str(i) for i in tempRes]
                res.append("".join(s))
                return

            for i in range(10):
                # situation of more than 1 digit and the diff is not k
                if len(tempRes) != 0 and abs(i - tempRes[-1]) != k:
                    continue
                if i == 0 and len(tempRes) == 0:
                    continue
                tempRes.append(i)
                backtrack(tempRes)
                tempRes.pop()

        backtrack([])
        return res
