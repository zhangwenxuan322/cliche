# 326. Power of Three


import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and (math.log10(n)/math.log10(3)) % 1 == 0


sol = Solution()
print(sol.isPowerOfThree(0))
print(sol.isPowerOfThree(27))
print(sol.isPowerOfThree(243))
