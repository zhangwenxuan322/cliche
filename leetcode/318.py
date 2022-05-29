# 318. Maximum Product of Word Lengths
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_product = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                word_a = set(words[i])
                word_b = set(words[j])
                product = len(words[i]) * len(words[j])
                if len(word_a.intersection(word_b)) == 0 and product > max_product:
                    max_product = product
        return max_product

    def test(self):
        assert self.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]) == 16
        assert self.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]) == 4
        assert self.maxProduct(["a", "aa", "aaa", "aaaa"]) == 0
        assert self.maxProduct(["eae", "ea", "aaf", "bda", "fcf", "dc", "ac", "ce", "cefde", "dabae"]) == 15
        print("all tests passed!")


Solution().test()
