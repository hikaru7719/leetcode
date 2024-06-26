from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        s = 0
        d = {0: 1}

        for n in nums:
            s += n
            if s - k in d:
                count += d[s - k]

            if s not in d:
                d[s] = 1
            else:
                d[s] += 1
        return count
