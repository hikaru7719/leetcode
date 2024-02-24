import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while self.k < len(self.nums):
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if self.k < len(self.nums):
            heapq.heappop(self.nums)
        return self.nums[0]
