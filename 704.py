# 704. Binary Search
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = int(start + (end - start) / 2)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def test(self):
        assert self.search(nums=[-1, 0, 3, 5, 9, 12], target=9) == 4
        assert self.search(nums=[-1, 0, 3, 5, 9, 12], target=2) == -1
        print("all tests passed!")


Solution().test()
