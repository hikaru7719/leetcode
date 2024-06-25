from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        index_map = {}
        counter = 0
        for e in emails:
            plus = False
            unique_mail: List[str] = []
            for i, c in enumerate(e):
                if c == "@":
                    unique_mail.append(e[i:])
                    break
                if plus:
                    continue
                if c == ".":
                    continue
                if c == "+":
                    plus = True
                    continue
                else:
                    unique_mail.append(c)
            mail_str = "".join(unique_mail)
            if mail_str not in index_map:
                index_map[mail_str] = True
                counter += 1

        return counter
