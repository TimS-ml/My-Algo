# https://leetcode-cn.com/problems/bold-words-in-string/
# See question 616


class Solution:
    def boldWords(self, words, S: str) -> str:
        mark = [0] * len(S)
        for d in words:
            pos = S.find(d)
            while pos != -1:  # .find return -1 when not find
                mark[pos:pos+len(d)] = [1] * len(d)
                pos = S.find(d, pos + 1)  # s.find(value, start, end)

        ans = []
        for i in range(len(S)):
            if mark[i] and (i == 0 or not mark[i-1]):
                ans.append("<b>")
            ans.append(S[i])
            if mark[i] and (i == len(S)-1 or not mark[i+1]):
                ans.append("</b>")
        return "".join(ans)


# words, S
IN = [(["ab","bc"], "aabcd")]
useSet = 0
print(IN[useSet][0], IN[useSet][1])
print(Solution().boldWords(IN[useSet][0], IN[useSet][1]))

