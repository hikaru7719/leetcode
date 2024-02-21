# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        result_head = head
        result = result_head
        while head is not None:
            if result.val != head.val:
                result.next = head
                result = result.next
            head = head.next
        result.next = None
        return result_head
