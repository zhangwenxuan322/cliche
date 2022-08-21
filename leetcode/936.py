# 936. Stamping The Sequence

from typing import List


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n, m = len(stamp), len(target)
        s = set()
        for i in range(n):
            for j in range(n-i):
                s.add('#'*i + stamp[i:n-j] + '#'*j)
        end = '#'*m
        res = []
        while target != end:
            check = False
            for i in range(m-n+1):
                if target[i:i+n] in s:
                    target = target[:i] + '#'*n + target[i+n:]
                    res.append(i)
                    check = True
            for i in range(m-n+1, -1, -1):
                if target[i:i+n] in s:
                    target = target[:i] + '#'*n + target[i+n:]
                    res.append(i)
                    check = True
            if not check:
                return []
        return res[::-1]
