# 581. Shortest Unsorted Continuous Subarray
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # Find right limit of the subarray. Traverse array from left to right
        right_ptr = 0
        big = nums[0]
        for i in range(len(nums)):
            if nums[i] < big:
                # a number smaller than what we have seen -> need sorting
                right_ptr = i
            else:
                big = nums[i]

        # Find left limit of the subarray. Traverse array from right to left
        left_ptr = 0
        small = nums[-1]
        for i in reversed(range(len(nums))):
            if nums[i] > small:
                # a number bigger than what we have seen -> need sorting
                left_ptr = i
            else:
                small = nums[i]

        if right_ptr == left_ptr:
            return 0
        return right_ptr - left_ptr + 1

    def test(self):
        assert self.findUnsortedSubarray(nums=[2, 6, 4, 8, 10, 9, 15]) == 5
        assert self.findUnsortedSubarray(nums=[1, 2, 3, 4]) == 0
        assert self.findUnsortedSubarray(nums=[0]) == 0
        print("all tests passed!")


Solution().test()
