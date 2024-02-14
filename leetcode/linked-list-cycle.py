from typing import Optional


class ListNode(object):
    def __init__(self, x: int):
        self.val = x
        self.next = None
        self.count = 0

class Solution(object):
    def __init__(self) :
        self.store= {}

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        if head in self.store:
            return True
        self.store[head] = True
        return self.hasCycle(head.next)
