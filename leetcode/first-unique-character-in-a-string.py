class Solution:
    def firstUniqChar(self, s: str) -> int:
        index_map = {}
        for ss in s:
            if ss not in index_map:
                index_map[ss] = 1
            else:
                index_map[ss] += 1
        for i, ss in enumerate(s):
            if index_map[ss] == 1:
                return i
        return -1
