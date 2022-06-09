# 167. Two Sum II - Input Array Is Sorted
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                l += 1
            else:
                r -= 1

    def test(self):
        assert self.twoSum(numbers=[2, 7, 11, 15], target=9) == [1, 2]
        assert self.twoSum(numbers=[2, 3, 4], target=6) == [1, 3]
        assert self.twoSum(numbers=[-1, 0], target=-1) == [1, 2]
        print("all tests passed!")


Solution().test()
