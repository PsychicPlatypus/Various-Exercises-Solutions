from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.sums = []

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root.val:
            return False

        self.sum_of_all_trees(root)
        return targetSum in self.sums

    def sum_of_all_trees(self, root):
        path = []
        self.append_sum_array(root, path)

    def append_sum_array(self, node, path):
        if node is not None:
            path.append(node.val)

            # leaf
            if node.left is None and node.right is None:
                self.sums.append(sum(list(path)))

            self.append_sum_array(node.left, path)
            self.append_sum_array(node.right, path)

            path.pop()


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)

print(Solution().hasPathSum(root, 6))
