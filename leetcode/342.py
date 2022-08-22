# 342. Power of Four

from math import log


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and log(n, 4).is_integer()
