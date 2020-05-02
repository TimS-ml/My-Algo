# https://leetcode-cn.com/problems/group-shifted-strings/

from typing import List
import collections


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for s in strings:
            key = self.getKey(s)
            dic[key].append(s)

        return [val for val in dic.values()]

    def getKey(self, s) -> str:
        # a-> 0, b = 1, z-> 25
        # z - a = 25
        # ( a - b  + 26 ) % 26 = 25
        ans = ''
        for i in range(1, len(s)):
            gap_str = str((ord(s[i]) - ord(s[i - 1]) + 26) % 26)
            ans += gap_str.zfill(2)
        return ans


# [["ayz"],["abc","bcd"]]
string = ["abc", "bcd", "ayz"]
print(Solution().groupStrings(string))

