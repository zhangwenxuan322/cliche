# 74. Search a 2D Matrix
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix)
        if height == 1:
            if target in matrix[0]:
                return True
            else:
                return False
        t_row = height - 1
        for i in range(height):
            if target < matrix[i][0]:
                t_row = i - 1
                break
            elif target == matrix[i][0]:
                return True
        if t_row < 0:
            return False
        if target in matrix[t_row]:
            return True
        return False

    def test(self):
        assert self.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3) is True
        assert self.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13) is False
        print("all tests passed!")


Solution().test()
