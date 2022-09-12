# 948. Bag of Tokens

from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        beg, end, S, max_S = 0, len(tokens) - 1, 0, 0
        while beg <= end:
            if tokens[beg] <= power:
                power -= tokens[beg]
                S += 1
                max_S = max(max_S, S)
                beg += 1
            elif S >= 1:
                power += tokens[end]
                S -= 1
                end -= 1
            else:
                break
        return max_S
