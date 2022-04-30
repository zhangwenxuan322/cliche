# 399. Evaluate Division
from collections import defaultdict, deque
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for ([x, y], value) in zip(equations, values):
            graph[x][y] = value
            graph[y][x] = 1 / value

        def find_prod(s, e):
            if s not in graph or e not in graph:
                return -1.0
            if s == e: return 1.0
            q = deque([(s, 1.0)])
            visited = {s}
            while q:
                n, curr = q.popleft()
                for child, value in graph[n].items():
                    if child in visited:
                        continue
                    nc = curr * value
                    if child == e:
                        return nc
                    graph[s][child] = nc
                    graph[child][s] = 1 / nc
                    visited.add(child)
                    q.append((child, nc))
            return -1.0

        return [find_prod(s, e) for [s, e] in queries]

    def test(self):
        assert self.calcEquation(equations=[["a", "b"], ["b", "c"]], values=[2.0, 3.0],
                                 queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]) == [6.00000,
                                                                                                           0.50000,
                                                                                                           -1.00000,
                                                                                                           1.00000,
                                                                                                           -1.00000]
        assert self.calcEquation(equations=[["a", "b"], ["b", "c"], ["bc", "cd"]], values=[1.5, 2.5, 5.0],
                                 queries=[["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]) == [3.75000, 0.40000,
                                                                                                   5.00000, 0.20000]
        print("all tests passed!")


Solution().test()
