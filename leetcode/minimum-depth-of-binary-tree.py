# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root and root.left is None and root.right is None:
            return 1
        elif root and root.left and not root.right:
            return self.minDepth(root.left) + 1
        elif root and root.right and not root.left:
            return self.minDepth(root.right) + 1
        elif root and root.right and root.left:
            return min(self.minDepth(root.left) + 1, self.minDepth(root.right) + 1)
        else:
            return 0
