# 344. Reverse String
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

    def test(self):
        list1 = ["h", "e", "l", "l", "o"]
        self.reverseString(list1)
        assert list1 == ["o", "l", "l", "e", "h"]
        list2 = ["H", "a", "n", "n", "a", "h"]
        self.reverseString(list2)
        assert list2 == ["h", "a", "n", "n", "a", "H"]
        print("all tests passed!")


Solution().test()
