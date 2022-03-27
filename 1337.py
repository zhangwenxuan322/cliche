# 1337. The K Weakest Rows in a Matrix
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        c = []
        for i in range(len(mat)):
            c.append([i, sum(mat[i])])
        c = sorted(c, key=lambda m: m[1])
        res = []
        for i in range(k):
            res.append(c[i][0])
        return res

    def test(self):
        assert self.kWeakestRows(mat=
                                 [[1, 1, 0, 0, 0],
                                  [1, 1, 1, 1, 0],
                                  [1, 0, 0, 0, 0],
                                  [1, 1, 0, 0, 0],
                                  [1, 1, 1, 1, 1]],
                                 k=3) == [2, 0, 3]
        assert self.kWeakestRows(mat=
                                 [[1, 0, 0, 0],
                                  [1, 1, 1, 1],
                                  [1, 0, 0, 0],
                                  [1, 0, 0, 0]],
                                 k=2) == [0, 2]
        print("all tests passed!")


Solution().test()
