# https://leetcode-cn.com/problems/reorder-data-in-log-files/

from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let = filter(lambda x: x[x.find(" ") + 1].isalpha(), logs)
        dig = filter(lambda x: x[x.find(" ") + 1].isdigit(), logs)
        # same as sol 0
        return sorted(let, key=lambda x:
                      (x[x.find(" "):], x[:x.find(" ")])) + list(dig)


# logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
logs = [
    "a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo",
    "a2 act car"
]  # tie

print(Solution().reorderLogFiles(logs))
