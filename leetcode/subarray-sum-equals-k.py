from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        length = len(nums)
        for i in range(1, 2**length + 1):
            sum = 0
            for j in range(length):
                if i & 1 << j != 0:
                    sum += nums[j]
            if sum == k:
                count += 1
        return count
