# 871. Minimum Number of Refueling Stops

from heapq import heappop, heappush
from math import inf
from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target, inf])
        fuel, count, prev = startFuel, 0, 0
        regrets = []
        for pos, gas in stations:
            dist, prev = pos - prev, pos
            while regrets and fuel < dist:
                fuel += -heappop(regrets)
                count += 1
            if fuel < dist: return -1
            fuel -= dist
            heappush(regrets, -gas)
        return count

