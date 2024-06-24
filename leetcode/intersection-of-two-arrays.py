from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index_map = {n: True for n in nums1}
        return list({n for n in nums2 if n in index_map})
