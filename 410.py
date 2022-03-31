# 410. Split Array Largest Sum
from collections import defaultdict
from typing import List


class Solution:
    def is_valid(self, nums, m, mid):
        # assume mid is < max(nums)
        cuts, curr_sum = 0, 0
        for x in nums:
            curr_sum += x
            if curr_sum > mid:
                cuts, curr_sum = cuts + 1, x
        subs = cuts + 1
        return subs <= m

    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        low, high, ans = max(nums), sum(nums), -1
        while low <= high:
            mid = (low + high) // 2
            if self.is_valid(nums, m, mid):  # can you make at-most m sub-arrays with maximum sum atmost mid
                ans, high = mid, mid - 1
            else:
                low = mid + 1
        return ans

    def test(self):
        assert self.splitArray(nums=[7, 2, 5, 10, 8], m=2) == 18
        assert self.splitArray(nums=[1, 2, 3, 4, 5], m=2) == 9
        assert self.splitArray(nums=[1, 4, 4], m=3) == 4
        print("all tests passed!")


Solution().test()
