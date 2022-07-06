# 509. Fibonacci Number
from functools import cache


class Solution:
    @cache
    def fib(self, n: int) -> int:
        return n if n <= 1 else self.fib(n - 1) + self.fib(n - 2)
