# 473. Matchsticks to Square

from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        def dfs(nums, pos, target):
            if pos == len(nums):
                return True
            for i in range(4):
                if target[i] >= nums[pos]:
                    target[i] -= nums[pos]
                    if dfs(nums, pos+1, target):
                        return True
                    target[i] += nums[pos]
            return False
        if len(matchsticks) < 4:
            return False
        numSum = sum(matchsticks)
        matchsticks.sort(reverse=True)
        if numSum % 4 != 0:
            return False
        target = [numSum/4] * 4
        return dfs(matchsticks, 0, target)
