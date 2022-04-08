# 703. Kth Largest Element in a Stream
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)
        self.nums.reverse()

    def add(self, val: int) -> int:
        if len(self.nums) == 0:
            self.nums.append(val)
        else:
            if val <= self.nums[len(self.nums) - 1]:
                self.nums.append(val)
            else:
                for i in range(len(self.nums)):
                    if self.nums[i] < val:
                        self.nums.insert(i, val)
                        break
        return self.nums[self.k - 1]


# Your KthLargest object will be instantiated and called as such:
kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))
print(kthLargest.add(5))
print(kthLargest.add(10))
print(kthLargest.add(9))
print(kthLargest.add(4))
