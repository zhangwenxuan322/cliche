# 47. Permutations II
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def rotate(nums, l):
            tmp = nums[l]
            i = l + 1
            while i < n:
                nums[i - 1] = nums[i]
                i += 1
            nums[-1] = tmp

        def dfs(nums, l):
            if l == n - 1:
                res.append(list(nums))
                return
            for i in range(l, n):
                if i > l and nums[i] == nums[l]: continue
                nums[l], nums[i] = nums[i], nums[l]  # swap
                dfs(nums, l + 1)  # note now we're passing by reference
            # recover
            rotate(nums, l)

        nums.sort()
        dfs(nums, 0)
        return res
