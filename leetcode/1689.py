# 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers

class Solution:
    def minPartitions(self, n: str) -> int:
        return max(int(i) for i in n)


print(Solution().minPartitions("32"))
