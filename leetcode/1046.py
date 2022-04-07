# 1046. Last Stone Weight
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        sorted_arr = sorted(stones)
        sorted_arr.reverse()
        while len(sorted_arr) > 1:
            first = sorted_arr[0]
            second = sorted_arr[1]
            sorted_arr.remove(first)
            sorted_arr.remove(second)
            if second < first:
                sorted_arr.append(first - second)
            sorted_arr = sorted(sorted_arr)
            sorted_arr.reverse()
        if len(sorted_arr) == 0:
            return 0
        else:
            return sorted_arr[0]

    def test(self):
        assert self.lastStoneWeight(stones=[2, 7, 4, 1, 8, 1]) == 1
        assert self.lastStoneWeight(stones=[1]) == 1
        print("all tests passed!")


Solution().test()
