# 844. Backspace String Compare
from typing import List


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_tmp = []
        t_tmp = []
        for c in s:
            if c == "#" and len(s_tmp) != 0:
                del s_tmp[len(s_tmp) - 1]
            else:
                if c != "#":
                    s_tmp.append(c)
        for c in t:
            if c == "#" and len(t_tmp) != 0:
                del t_tmp[len(t_tmp) - 1]
            else:
                if c != "#":
                    t_tmp.append(c)
        return s_tmp == t_tmp

    def test(self):
        assert self.backspaceCompare(s="ab#c", t="ad#c") is True
        assert self.backspaceCompare(s="ab##", t="c#d#") is True
        assert self.backspaceCompare(s="a#c", t="b") is False
        assert self.backspaceCompare(s="y#fo##f", t="y#f#o##f") is True
        print("all tests passed!")


Solution().test()
