# 623. Add One Row to Tree

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], v: int, d: int) -> Optional[TreeNode]:
        dummy, dummy.left = TreeNode(None), root
        row = [dummy]
        for _ in range(d - 1):
            row = [kid for node in row for kid in (
                node.left, node.right) if kid]
        for node in row:
            node.left, node.left.left = TreeNode(v), node.left
            node.right, node.right.right = TreeNode(v), node.right
        return dummy.left
