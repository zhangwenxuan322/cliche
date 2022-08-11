# 98. Validate Binary Search Tree

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def Helper(root, left, right):
            if root is None:
                return True
            rootVal = root.val
            if not (left < rootVal < right):
                return False
            return Helper(root.left, left, rootVal) and Helper(root.right, rootVal, right)

        return Helper(root, float('-inf'), float('inf'))
