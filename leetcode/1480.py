# 1480. Running Sum of 1d Array
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.append(sum(nums[:i + 1]))
        return res

    def test(self):
        assert self.runningSum(nums=[1, 2, 3, 4]) == [1, 3, 6, 10]
        assert self.runningSum(nums=[1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
        assert self.runningSum(nums=[3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
        print("all tests passed!")


Solution().test()
