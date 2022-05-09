# 17. Letter Combinations of a Phone Number
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
                :type digits: str
                :rtype: List[str]
                """
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        res = []
        if len(digits) == 0:
            return res

        self.dfs(digits, 0, dic, '', res)
        return res

    def dfs(self, nums, index, dic, path, res):
        if index >= len(nums):
            res.append(path)
            return
        string1 = dic[nums[index]]
        for i in string1:
            self.dfs(nums, index + 1, dic, path + i, res)

    def test(self):
        assert self.letterCombinations(digits="23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        assert self.letterCombinations(digits="") == []
        assert self.letterCombinations(digits="2") == ["a", "b", "c"]
        print("all tests passed!")


Solution().test()
