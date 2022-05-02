# 905. Sort Array By Parity
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] % 2 == 0:
                i += 1
                continue
            if nums[j] % 2 != 0:
                j -= 1
                continue
            if nums[i] % 2 != 0 and nums[j] % 2 == 0:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
        return nums


sol = Solution()
print(sol.sortArrayByParity(nums=[3, 1, 2, 4]))
print(sol.sortArrayByParity([0]))
