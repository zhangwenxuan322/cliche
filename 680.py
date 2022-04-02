# 680. Valid Palindrome II

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                delete_i = s[i + 1:j + 1]
                delete_j = s[i:j]
                return self._isPalindrome(delete_i) or self._isPalindrome(delete_j)
            i += 1
            j -= 1
        return True

    def _isPalindrome(self, s):
        return s == s[::-1]

    def test(self):
        assert self.validPalindrome(s="aba") is True
        assert self.validPalindrome(s="abca") is True
        assert self.validPalindrome(s="abc") is False
        print("all tests passed!")


Solution().test()
