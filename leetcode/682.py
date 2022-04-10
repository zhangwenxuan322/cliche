# 682. Baseball Game
from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        for op in ops:
            if op == '+':
                res.append(res[-1] + res[-2])
            elif op == 'D':
                res.append(res[-1] * 2)
            elif op == 'C':
                del res[-1]
            else:
                res.append(int(op))
        return sum(res)

    def test(self):
        assert self.calPoints(ops=["5", "2", "C", "D", "+"]) == 30
        assert self.calPoints(ops=["5", "-2", "4", "C", "D", "9", "+", "+"]) == 27
        assert self.calPoints(ops=["1"]) == 1
        print("all tests passed!")


Solution().test()
