# 347. Top K Frequent Elements
from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = defaultdict(int)
        for n in nums:
            dict[n] += 1
        s = sorted(dict.items(), key=lambda i: i[1], reverse=True)
        res = []
        for i in range(k):
            res.append(s[i][0])
        return res

    def test(self):
        assert self.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2) == [1, 2]
        assert self.topKFrequent(nums=[1], k=1) == [1]
        print("all tests passed!")


Solution().test()
