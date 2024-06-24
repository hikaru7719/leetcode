from typing import Dict, List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_map: Dict[str, List[str]] = {}
        for s in strs:
            sort_str = "".join(sorted(list(s)))
            if sort_str in result_map:
                result_map[sort_str].append(s)
            else:
                result_map[sort_str] = [s]

        return [result_map[key] for key in result_map]
