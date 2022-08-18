# 1338. Reduce Array Size to The Half

from typing import Counter, List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:


        n = len(arr)
        
        bucket = [0]*(n+1)
        for c in Counter(arr).values():
            bucket[c] += 1
        
        half = len(arr) // 2
        
        ans = 0
        count = 0

        for i in range(n, -1, -1):
            
            while bucket[i]:
                ans += 1
                count += i
                
                if count >= half:
                    return ans
                
                bucket[i] -= 1
        
        return ans