# https://leetcode-cn.com/problems/add-bold-tag-in-string/
# official answer is not cool
# [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
# [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D


import itertools


class Solution:
    def addBoldTag(self, s, dict) -> str:
        mark = [0] * len(s)
        # for i in range(len(s)):
        #     perfix = s[i:]
        #     for word in dict:
        #         # The startswith() method returns a boolean
        #         if perfix.startswith(word):
        #             for j in range(i, min(i + len(word), len(s))):
        #                 mark[j] = 1
        for d in dict:
            pos = s.find(d)
            while pos != -1:
                mark[pos:pos+len(d)] = [1] * len(d)
                pos = s.find(d, pos + 1)

        ans = []
        # groupby(data, keyfunc)
        for k, g in itertools.groupby(zip(s, mark), lambda z: z[1]):
            print(k, g)
            if k:
                ans.append("<b>")
            ans.append("".join(z[0] for z in g))
            if k:
                ans.append("</b>")
        return "".join(ans), mark


s = "abcxyz123"
dic = ["abc", "cxy", "3"]
print(Solution().addBoldTag(s, dic))
