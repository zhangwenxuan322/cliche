# 99. Recover Binary Search Tree

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first = None
        self.second = None
        self.prev = TreeNode(-2 ** 32)
        self.traverse(root)
        tmp = self.first.val
        self.first.val = self.second.val
        self.second.val = tmp

    def traverse(self, root: Optional[TreeNode]):
        if not root:
            return
        self.traverse(root.left)
        if not self.first and self.prev.val >= root.val:
            self.first = self.prev
        if self.first and self.prev.val >= root.val:
            self.second = root
        self.prev = root
        self.traverse(root.right)
