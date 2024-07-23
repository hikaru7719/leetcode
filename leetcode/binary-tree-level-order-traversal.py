# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        levels = [[root.val]]
        temp: deque[TreeNode] = deque()

        while q:
            node = q.popleft()

            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)

            if not q:
                if temp:
                    levels.append([n.val for n in temp])
                q = temp
                temp = deque()

        return levels
