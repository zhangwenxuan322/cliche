# 11. Container With Most Water
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max = 0
        while l < r:
            area = (r - l) * min(height[l], height[r])
            if area > max:
                max = area
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max

    def test(self):
        assert self.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
        assert self.maxArea(height=[1, 1]) == 1
        print("all tests passed!")


Solution().test()
