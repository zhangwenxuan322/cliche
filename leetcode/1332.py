# 1332. Remove Palindromic Subsequences

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif s == s[::-1]:
            return 1
        else:
            return 2

    def test(self):
        assert self.removePalindromeSub(s="ababa") == 1
        assert self.removePalindromeSub(s="abb") == 2
        assert self.removePalindromeSub(s="baabb") == 2
        print("all tests passed!")


Solution().test()
