# 1658. Minimum Operations to Reduce X to Zero
from itertools import accumulate
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        cumsum = [0] + list(accumulate(nums))
        dic = {c: i for i, c in enumerate(cumsum)}
        goal = cumsum[-1] - x
        ans = -float("inf")

        if goal < 0: return -1

        for num in dic:
            if num + goal in dic:
                ans = max(ans, dic[num + goal] - dic[num])

        return len(nums) - ans if ans != -float("inf") else -1
