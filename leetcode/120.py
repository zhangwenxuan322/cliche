# 120. Triangle
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        last = len(triangle) - 1
        for row in (triangle[:-1])[::-1]:  # begin 2nd last row from the end
            for i in range(len(row)):
                row[i] = row[i] + min(triangle[last][i], triangle[last][i + 1])
            last -= 1

        return triangle[0][0]
