# 304. Range Sum Query 2D - Immutable
from typing import List


class NumMatrix:

    def __init__(self, matrix):
        if not matrix:
            return
        n, m = len(matrix), len(matrix[0])
        self.sum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                self.sum[i + 1][j + 1] = self.sum[i + 1][j] + self.sum[i][j + 1] + matrix[i][j] - self.sum[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        return self.sum[row2 + 1][col2 + 1] - self.sum[row1][col2 + 1] - self.sum[row2 + 1][col1] + self.sum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(obj.sumRegion(2, 1, 4, 3))
print(obj.sumRegion(1, 1, 2, 2))
print(obj.sumRegion(1, 2, 2, 4))
