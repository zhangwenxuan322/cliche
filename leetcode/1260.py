# 1260. Shift 2D Grid
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        while k > 0:
            k -= 1
            tmp = []
            for i in range(m):
                tmp_ele = []
                for j in range(n):
                    last_i = i
                    last_j = j - 1
                    if last_i == 0 and last_j < 0:
                        tmp_ele.append(grid[m - 1][n - 1])
                    elif last_i != 0 and last_j < 0:
                        tmp_ele.append(grid[i - 1][n - 1])
                    else:
                        tmp_ele.append(grid[last_i][last_j])
                tmp.append(tmp_ele)
            grid = tmp
        return grid

    def test(self):
        assert self.shiftGrid(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=1) == [[9, 1, 2], [3, 4, 5], [6, 7, 8]]
        assert self.shiftGrid(grid=[[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], k=4) == [
            [12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]]
        assert self.shiftGrid(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=9) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        print("all tests passed!")


Solution().test()
