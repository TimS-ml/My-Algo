# https://leetcode-cn.com/problems/group-shifted-strings/
# this is smart, find ord difference inside single str

from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dic = {}
        for s in strings:
            diff = []
            prev = s[0]
            for char in s:
                index = (ord(char) - ord(prev)) % 26
                diff.append(index)
                prev = char
            print(diff)
            diff = tuple(diff)  # because we need to do dic[diff]
            if diff in dic:
                dic[diff].append(s)
            else:
                dic[diff] = [s]
        print(dic)
        return list(dic.values())


# [["ayz"],["abc","bcd"]]
strings = ["abc", "bcd", "ayz"]
print(Solution().groupStrings(strings))

