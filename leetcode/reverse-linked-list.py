from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.stack = deque([])

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        first = result

        while head:
            self.stack.append(head.val)
            head = head.next

        while self.stack:
            result.next = ListNode(self.stack.pop())
            result = result.next

        return first.next
