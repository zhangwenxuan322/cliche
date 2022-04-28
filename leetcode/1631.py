# 1631. Path With Minimum Effort
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        neibs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(LIMIT, x, y):
            visited.add((x, y))
            for dx, dy in neibs:
                if 0 <= dx + x < m and 0 <= dy + y < n and (dx + x, dy + y) not in visited:
                    if abs(heights[x][y] - heights[dx + x][dy + y]) <= LIMIT:
                        dfs(LIMIT, dx + x, dy + y)

        beg, end = -1, max(max(heights, key=max))
        while beg + 1 < end:
            mid = (beg + end) // 2
            visited = set()
            dfs(mid, 0, 0)
            if (m - 1, n - 1) in visited:
                end = mid
            else:
                beg = mid

        return end

    def test(self):
        assert self.minimumEffortPath(heights=[[1, 2, 2], [3, 8, 2], [5, 3, 5]]) == 2
        assert self.minimumEffortPath(heights=[[1, 2, 3], [3, 8, 4], [5, 3, 5]]) == 1
        print("all tests passed!")


Solution().test()
