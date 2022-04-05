# 1029. Two City Scheduling
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # If all the people travels to the cityA then total cost:
        totalA = 0
        for costA, _ in costs:
            totalA += costA

        # If all the people wish to travel to cityB instead of cityA then the difference in cost would be:
        difference = [costB - costA for costA, costB in costs]

        """
            Since in both the cities the number of people travelling should be equal and their total cost should be minimum,
            So if we move half of the people from cityA to cityB having minimum difference among all the people then the total cost would be the minimum.
        """
        # Total cost of people travelling to cityB instead of cityA having minimum difference:
        totalB = sum(sorted(difference)[:len(costs) // 2])

        # Total cost of travelling for both the cities
        return totalA + totalB

    def test(self):
        assert self.twoCitySchedCost([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]) == 1859
        assert self.twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]) == 110
        assert self.twoCitySchedCost(
            [[515, 563], [451, 713], [537, 709], [343, 819], [855, 779], [457, 60], [650, 359], [631, 42]]) == 3086
        print("all tests passed!")


Solution().test()
