# 867. Transpose Matrix
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(matrix[0])):
            tmp = []
            for j in range(len(matrix)):
                if i != j:
                    tmp.append(matrix[j][i])
                else:
                    tmp.append(matrix[i][j])
            res.append(tmp)
        return res

    def test(self):
        assert self.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        assert self.transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
        print("all tests passed!")


Solution().test()
