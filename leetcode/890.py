# 890. Find and Replace Pattern

from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(w1:str, w2:str) -> bool:
            if len(w1) != len(w2):
                return False
            mp1, mp2 = {}, {}
            for a,b in zip(w1, w2):
                mp1[a] = b
                mp2[b] = a
            for a,b in zip(w1, w2):
                if mp1[a] != b or mp2[b] != a :
                    return False
            return True
        return [w for w in words if match(w, pattern)]
        

