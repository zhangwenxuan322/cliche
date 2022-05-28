# 268. Missing Number
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n + 1):
            if i not in nums:
                return i

    def test(self):
        assert self.missingNumber([3, 0, 1]) == 2
        assert self.missingNumber([0, 1]) == 2
        assert self.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
        print("all tests passed!")


Solution().test()
