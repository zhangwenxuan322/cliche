# 743. Network Delay Time
import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        q, t, adj = [(0, k)], {}, collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        while q:
            time, node = heapq.heappop(q)
            if node not in t:
                t[node] = time
                for v, w in adj[node]:
                    heapq.heappush(q, (time + w, v))
        return max(t.values()) if len(t) == n else -1
