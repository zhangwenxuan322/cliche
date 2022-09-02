# 637. Average of Levels in Binary Tree

# Definition for a binary tree node.
from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levelSums = defaultdict(float)
        levelCounts = defaultdict(int)

        def dfs(node, h):
            if not node:
                return
            levelSums[h] += node.val
            levelCounts[h] += 1
            dfs(node.left, h+1)
            dfs(node.right, h+1)

        dfs(root, 0)
        return[levelSums[i]/levelCounts[i] for i in range(len(levelSums))]
