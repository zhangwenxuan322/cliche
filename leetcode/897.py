# 897. Increasing Order Search Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root, arr):
        if root is None:
            return
        self.dfs(root.left, arr)
        arr.append(root.val)
        self.dfs(root.right, arr)

    def increasingBST(self, root):
        arr = []
        self.dfs(root, arr)
        ans = cur = TreeNode()
        for v in arr:
            cur.right = TreeNode(v)
            cur = cur.right

        return ans.right
