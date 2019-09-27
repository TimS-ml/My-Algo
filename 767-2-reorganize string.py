# https://leetcode-cn.com/problems/reorganize-string/
# https://leetcode.com/problems/reorganize-string/solution/


class Solution:
    def reorganizeString(self, S: str) -> str:
        length = len(S)
        dic = []
        for c, x in sorted((S.count(x), x) for x in set(S)):
            if c > (length+1)/2: return ""
            dic.extend(c*x)
        ans = [None] * length
        ans[::2], ans[1::2] = dic[int(length/2):], dic[:int(length/2)]
        return "".join(ans)


S1 = "aaab"
S2 = "aab"
S3 = "a"
print(Solution().reorganizeString(S2))
