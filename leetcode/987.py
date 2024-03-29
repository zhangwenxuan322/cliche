# 987. Vertical Order Traversal of a Binary Tree

# Definition for a binary tree node.
from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = defaultdict(list)

        queue = [(root, 0, 0)]

        while queue:
            node, pos, depth = queue.pop(0)
            if not node:
                continue
            results[(pos, depth)].append(node.val)
            results[(pos, depth)].sort()
            queue.extend([(node.left, pos-1, depth+1),
                         (node.right, pos+1, depth+1)])

        res = defaultdict(list)
        keys = sorted(list(results.keys()), key=lambda x: (x[0], x[1]))

        for k in keys:
            pos, depth = k
            res[pos].extend(results[k])

        return res.values()
