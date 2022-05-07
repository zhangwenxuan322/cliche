# 456. 132 Pattern
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        s3 = - 10 ** 9 + 1
        for n in nums[::-1]:
            if n < s3:
                return True
            while stack and stack[-1] < n:
                s3 = stack.pop()
            stack.append(n)
        return False

    def test(self):
        assert self.find132pattern(nums=[1, 2, 3, 4]) is False
        assert self.find132pattern(nums=[3, 1, 4, 2]) is True
        assert self.find132pattern(nums=[-1, 3, 2, 0]) is True
        print("all tests passed!")


Solution().test()
