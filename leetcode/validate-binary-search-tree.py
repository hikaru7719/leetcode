# Definition for a binary tree node.
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        INF = sys.maxsize

        def helper(node: Optional[TreeNode], lower: int, upper: int) -> bool:
            if not node:
                return True

            if lower < node.val < upper:
                return helper(node.left, lower, node.val) and helper(
                    node.right, node.val, upper
                )

            else:
                return False

        return helper(root, -INF, INF)
