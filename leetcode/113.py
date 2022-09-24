# 113. Path Sum II

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        if root.left == None and root.right == None:
            if targetSum == root.val:
                return [[root.val]]
            else:
                return []
        a = self.pathSum(root.left, targetSum - root.val) + \
            self.pathSum(root.right, targetSum - root.val)
        return [[root.val] + i for i in a]
