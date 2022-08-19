# 659. Split Array into Consecutive Subsequences

from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        len1 = len2 = absorber = 0
        prev_num = nums[0] - 1
        for streak_len, streak_num in Solution.get_streaks(nums):
            if streak_num == prev_num + 1:
                spillage = streak_len - len1 - len2
                if spillage < 0:
                    return False
                absorber = min(absorber, spillage)
                len1, len2, absorber = spillage - absorber, len1, absorber + len2
            else:
                if len1 or len2:
                    return False
                absorber = 0
            prev_num = streak_num
        return len1 == len2 == 0
    
    @staticmethod
    def get_streaks(nums: List[int]):
        streak_num = nums[0]
        streak_len = 0
        for num in nums:
            if num == streak_num:
                streak_len += 1
            else:
                yield streak_len, streak_num
                streak_num = num
                streak_len = 1
        yield streak_len, streak_num