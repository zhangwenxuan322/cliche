# 990. Satisfiability of Equality Equations

import collections
from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        graph = collections.defaultdict(set)
        notEquals = []

        def canMeet(u, target, visited):
            if u == target:
                return True
            visited.add(u)
            for v in graph[u]:
                if v in visited:
                    continue
                if canMeet(v, target, visited):
                    return True
            return False

        for eq in equations:
            if eq[1:3] == '!=':
                a, b = eq.split('!=')
                notEquals.append((a, b))
                continue
            u, v = eq.split('==')
            graph[u].add(v)
            graph[v].add(u)

        for u, v in notEquals:
            if canMeet(u, v, set()):
                return False
        return True
