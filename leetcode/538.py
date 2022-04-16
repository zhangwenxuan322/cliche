# 538. Convert BST to Greater Tree

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.val = 0

        def visit(root):
            if root:
                visit(root.right)
                root.val += self.val
                self.val = root.val
                visit(root.left)

        visit(root)
        return root
