# 1457. Pseudo-Palindromic Paths in a Binary Tree


# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root):
        if not root:
            return

        cur, pal = self.dict_freq[root.val], self.Pal

        self.Pal = self.Pal - 1 if cur == 1 else self.Pal + 1
        self.dict_freq[root.val] = (cur + 1) % 2

        if not root.left and not root.right and self.Pal <= 1:
            self.Res += 1

        self.dfs(root.left)
        self.dfs(root.right)

        self.Pal, self.dict_freq[root.val] = pal, cur

    def pseudoPalindromicPaths(self, root):
        self.dict_freq = defaultdict(int)
        self.Pal, self.Res = 0, 0
        self.dfs(root)
        return self.Res
