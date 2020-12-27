# https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/
# see 567, difference is we need return positon


class Solution:
    def findAnagrams(self, s: str, p: str):
        dic1, dic2 = dict(), dict()
        for st in p:
            dic1[st] = dic1.get(st, 0) + 1
        start, end = 0, 0
        res = []

        while end < len(s):
            dic2[s[end]] = dic2.get(s[end], 0) + 1
            if dic1 == dic2:
                res.append(start)

            end += 1

            # compare
            if end - start + 1 > len(p):
                dic2[s[start]] == 0:
                    del(dic2[s[start]])
                start += 1
        return res
