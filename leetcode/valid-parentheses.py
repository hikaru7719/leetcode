from collections import deque


class Solution:
    def __init__(self):
        self.stack = deque([])

    def isValid(self, s: str) -> bool:
        for ss in s:
            if ss == "{" or ss == "(" or ss == "[":
                self.stack.append(ss)
            else:
                if len(self.stack) == 0:
                    return False
                last = self.stack.pop()
                if (
                    (last == "{" and ss == "}")
                    or (last == "(" and ss == ")")
                    or (last == "[" and ss == "]")
                ):
                    continue
                else:
                    return False
        if 0 < len(self.stack):
            return False
        else:
            return True
