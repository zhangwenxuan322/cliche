# 458. Poor Pigs

from math import ceil, log


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return ceil(log(buckets) / log(minutesToTest / minutesToDie + 1))
