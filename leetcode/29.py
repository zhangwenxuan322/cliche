# 29. Divide Two Integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_minus = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
        ret = 0
        dividend, divisor = abs(dividend), abs(divisor)
        c, sub = 1, divisor

        while dividend >= divisor:
            if dividend >= sub:
                dividend -= sub
                ret += c
                sub = (sub << 1)
                c = (c << 1)
            else:
                sub = (sub >> 1)
                c = (c >> 1)

        if is_minus:
            ret = -ret
        return min(max(-2147483648, ret), 2147483647)

    def test(self):
        assert self.divide(dividend=10, divisor=3) == 3
        assert self.divide(dividend=7, divisor=-3) == -2
        print("all tests passed!")


Solution().test()
