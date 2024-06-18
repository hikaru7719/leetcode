import heapq
from typing import Dict, List, Tuple


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter: Dict[int, int] = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1

        heap: List[Tuple[int, int]] = []
        for n in counter.keys():
            if len(heap) < k:
                heapq.heappush(heap, (counter[n], n))
            else:
                heapq.heappushpop(heap, (counter[n], n))

        return list(map(lambda t: t[1], heap))
