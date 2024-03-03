from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        pass


def level_order_traversal(root: Node) -> list:
    if not root:
        return []

    elements = []

    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        elements.append(current.data)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return elements
