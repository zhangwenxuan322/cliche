# 287. Find the Duplicate Number
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] == nums[i + 1]:
                return nums[i]

    def test(self):
        assert self.findDuplicate(nums=[1, 3, 4, 2, 2]) == 2
        assert self.findDuplicate(nums=[3, 1, 3, 4, 2]) == 3
        print("all tests passed!")


Solution().test()
