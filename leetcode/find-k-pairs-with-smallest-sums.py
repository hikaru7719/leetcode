import heapq
from typing import List, Tuple


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        heap: List[Tuple[int, int]] = []
        for i in range(min(len(nums1), k)):
            heapq.heappush(heap, ((nums1[i] + nums2[0]), 0))

        result = []
        while 0 < k:
            (sum, index) = heapq.heappop(heap)
            result.append([sum - nums2[index], nums2[index]])

            if index + 1 < len(nums2):
                heapq.heappush(heap, (sum - nums2[index] + nums2[index + 1], index + 1))

            k -= 1
        return result
