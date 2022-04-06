# 923. 3Sum With Multiplicity
from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = [0 for i in range(0, 101)]
        for i in arr:
            count[i] += 1
        res = 0
        for i in range(0, 101):
            for j in range(i, 101):
                k = target - i - j
                if k < 0 or k > 100:
                    continue
                if i == j == k:
                    res += count[i] * (count[i] - 1) * (count[i] - 2) // 6
                elif i == j != k:
                    res += ((count[i] * (count[i] - 1)) // 2) * count[k]
                elif i < j < k:
                    res += count[i] * count[j] * count[k]
        return res % (10 ** 9 + 7)

    def test(self):
        assert self.threeSumMulti(arr=[1, 1, 2, 2, 3, 3, 4, 4, 5, 5], target=8) == 20
        assert self.threeSumMulti(arr=[1, 1, 2, 2, 2, 2], target=5) == 12
        assert self.threeSumMulti(arr=[0, 0, 0], target=0) == 1
        print("all tests passed!")


Solution().test()
