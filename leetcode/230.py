# 230. Kth Smallest Element in a BST

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = 0
        self.helper(root)
        return self.res

    def helper(self, root: Optional[TreeNode]):
        if not root:
            return
        self.helper(root.left)
        self.k -= 1
        if self.k == 0:
            self.res = root.val
        self.helper(root.right)
