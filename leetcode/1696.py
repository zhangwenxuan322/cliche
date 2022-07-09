# 1696. Jump Game VI

from collections import deque
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        deq, n = deque([0]), len(nums)

        for i in range(1, n):
            while deq and deq[0] < i - k: deq.popleft()
            nums[i] += nums[deq[0]]   
            while deq and nums[i] >= nums[deq[-1]]: deq.pop()
            deq.append(i)
            
        return nums[-1]

