from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {n: i for i, n in enumerate(nums)}
        for i, n in enumerate(nums):
            if target - n in index_map and i != index_map[target - n]:
                return [i, index_map[target - n]]
        return []
