from typing import Optional
from collections import deque


"""

        x(0, 0)
    x2(_, 1)      x1'(_, 1)
x3(_, 2)              x2'(_ 1)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        deepest = root.val

        while True:
            current = queue.pop(0)
            deepest = current.val

            if current.right != None:
                queue.append(current.right)
            elif current.left != None:
                queue.append(current.left)

            if queue == []:
                break

        return deepest
