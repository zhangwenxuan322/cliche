# 31. Next Permutation
# algorithm reference: https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = j = len(nums) - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        i -= 1
        if i == -1:
            nums.reverse()
            return
        while j > i and nums[j] <= nums[i]:
            j -= 1
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
        nums[i + 1:] = nums[i + 1:][::-1]

    def test(self):
        list1 = [1, 2, 3]
        self.nextPermutation(list1)
        assert list1 == [1, 3, 2]
        list2 = [3, 2, 1]
        self.nextPermutation(list2)
        assert list2 == [1, 2, 3]
        list3 = [1, 1, 5]
        self.nextPermutation(list3)
        assert list3 == [1, 5, 1]
        list4 = [1, 3, 2]
        self.nextPermutation(list4)
        assert list4 == [2, 1, 3]
        list5 = [1, 5, 1]
        self.nextPermutation(list5)
        assert list5 == [5, 1, 1]
        list6 = [5, 1, 1]
        self.nextPermutation(list6)
        assert list6 == [1, 1, 5]
        print("all tests passed!")


Solution().test()
