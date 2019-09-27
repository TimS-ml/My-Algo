# https://leetcode-cn.com/problems/assign-cookies/


class Solution:
    def findContentChildren(self, g, s) -> int:
        g.sort()  # kids
        s.sort()  # cookies
        i = 0
        for cookie in s:
            if i >= len(g):
                break
            if g[i] <= cookie:
                i += 1
        return i


g, s = [1,2], [1,2,3]
print(Solution().findContentChildren(g, s))
