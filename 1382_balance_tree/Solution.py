# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        vals = self.traverseBST(root)

        def createBST(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            left = createBST(l, m - 1)
            right = createBST(m + 1, r)
            return TreeNode(vals[m], left, right)

        return createBST(0, len(vals) - 1)

    def traverseBST(self, root: TreeNode) -> List[int]:
        if root:
            return (
                self.traverseBST(root.left) + [root.val] + self.traverseBST(root.right)
            )
        else:
            return []
