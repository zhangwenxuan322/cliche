# 59. Spiral Matrix II
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res, lo = [[n * n]], n * n
        while lo > 1:
            lo, hi = lo - len(res), lo
            # print(lo, hi)
            # print('res:', res)
            res = [[i for i in range(lo, hi)]] + [list(j) for j in zip(*res[::-1])]
            # print(res)
        return res

    def test(self):
        assert self.generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        assert self.generateMatrix(1) == [[1]]
        print("all tests passed!")


Solution().test()
