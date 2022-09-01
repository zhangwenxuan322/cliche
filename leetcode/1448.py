# 1448. Count Good Nodes in Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def recursive(node: TreeNode, max_till_now) -> int:
            if node == None:
                return 0
            max_till_now = max(max_till_now, node.val)
            return recursive(node.left, max_till_now) + recursive(node.right, max_till_now) + (1 if max_till_now == node.val else 0)
        return recursive(root, root.val)
