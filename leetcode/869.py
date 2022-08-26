# 869. Reordered Power of 2

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        i, arr = 0, []
        v = 2**i
        while v <= 10**9:
            arr.append(sorted(str(v)))
            i += 1
            v = 2**i
        return sorted(str(n)) in arr
