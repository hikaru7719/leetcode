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
        result = resultHead = None
        last = -200
        while head is not None:
            if last != head.val:
                if head.next is None:
                    if result is None:
                        result = head
                        resultHead = result
                    else:
                        result.next = head
                        result = result.next
                elif head.val != head.next.val:
                    if result is None:
                        result = head
                        resultHead = result
                    else:
                        result.next = head
                        result = result.next
            last = head.val
            head = head.next
        if result is not None:
            result.next = None
        return resultHead
