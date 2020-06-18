# https://leetcode-cn.com/problems/add-bold-tag-in-string/


class Solution:
    def addBoldTag(self, s, dict) -> str:
        mark = [0] * len(s)
        for d in dict:
            pos = s.find(d)
            while pos != -1:  # .find return -1 when not find
                mark[pos:pos + len(d)] = [1] * len(d)
                pos = s.find(d, pos + 1)  # s.find(value, start, end)

        ans = []
        for i in range(len(s)):
            if mark[i] and (i == 0 or not mark[i - 1]):
                ans.append("<b>")
            ans.append(s[i])
            if mark[i] and (i == len(s) - 1 or not mark[i + 1]):
                ans.append("</b>")
        return "".join(ans), mark


s = "abcxyz123"
dic = ["abc", "cxy", "3"]
print(Solution().addBoldTag(s, dic))
