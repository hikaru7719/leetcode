# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.cache = {}

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head in self.cache:
            return self.cache[head]
        self.cache[head] = head
        return self.detectCycle(head.next)
