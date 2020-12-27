# https://leetcode-cn.com/problems/reorder-data-in-log-files/
# https://leetcode.com/problems/reorder-data-in-log-files/discuss/352878/Python3-Sort-the-list-use-key

# all of the letter-logs come before any digit-log.
# letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.
# digit-logs should be put in their original order.

from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def f(log):
            id_, rest = log.split(" ", 1)
            # [1] 0 < 1: so letter-logs come before any digit-log
            # [2] rest and None The letter-logs are sorted lexicographically 词典上 by contend(rest),
            #     the digit-logs remain in the same order
            # [3] id_ and None The letter-logs are sorted lexicographically by contend(id_),
            #     the digit-logs remain in the same order (identifier used in case of ties)
            return (0, rest, id_) if rest[0].isalpha() else (1, )

        return sorted(logs, key=f)


# logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
logs = [
    "a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo",
    "a2 act car"
]  # tie

print(Solution().reorderLogFiles(logs))
