# 81. Search in Rotated Sorted Array II
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if target in nums:
            return True
        else:
            return False

    def test(self):
        assert self.search(nums=[2, 5, 6, 0, 0, 1, 2], target=0) == True
        assert self.search(nums=[2, 5, 6, 0, 0, 1, 2], target=3) == False
        print("all tests passed!")


Solution().test()
