# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        val_to_inorder_idx = {inorder[i]: i for i in range(len(inorder))}

        def buildTreePartition(preorder, inorder_start, inorder_end):
            if not preorder or inorder_start < 0 or len(inorder) < inorder_end:
                return None

            root_val = preorder[0]
            root_inorder_idx = val_to_inorder_idx[root_val]
            if inorder_end < root_inorder_idx or root_inorder_idx < inorder_start:
                return None

            root = TreeNode(preorder.pop(0))
            root.left = buildTreePartition(
                preorder, inorder_start, root_inorder_idx - 1
            )
            root.right = buildTreePartition(preorder, root_inorder_idx + 1, inorder_end)
            return root

        return buildTreePartition(preorder, 0, len(inorder) - 1)
