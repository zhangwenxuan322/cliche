# 814. Binary Tree Pruning

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        if self.pruneTree(root.left) is None:
            root.left = None
        if self.pruneTree(root.right) is None:
            root.right = None

        if root.val != 1 and root.left is None and root.right is None:
            root = None

        return root
