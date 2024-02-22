# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode()
        result = head
        add = 0
        fake = ListNode()
        while l1 or l2:
            if not l1:
                l1 = fake
            if not l2:
                l2 = fake
            current = ListNode((add + l1.val + l2.val) % 10)
            add = (add + l1.val + l2.val) // 10
            result.next = current
            result = current
            l1 = l1.next
            l2 = l2.next
        if add != 0:
            result.next = ListNode(add)
        return head.next
