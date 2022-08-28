# 1329. Sort the Matrix Diagonally

from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        num_cols = len(mat[0])
        num_rows = len(mat)
        unsorted = True

        while unsorted:
            unsorted = False
            for row in range(num_rows - 1):
                for col in range(num_cols - 1):
                    if mat[row][col] > mat[row+1][col+1]:
                        unsorted = True
                        mat[row][col], mat[row+1][col +
                                                  1] = mat[row+1][col+1], mat[row][col]

        return mat
