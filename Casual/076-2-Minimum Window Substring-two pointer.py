# https://leetcode-cn.com/problems/minimum-window-substring/


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        ans = ""
        dic = dict()

        # hash init
        for char in t:
            dic[char] = dic.get(char, 0) + 1
        print("dic:{}".format(dic))
        # in 076-1 we use deq[0] and deq[-1], start and end
        start, end = 0, 0
        minLength = len(s)
        score = 0

        while end < len(s):
            # duplicate
            if s[end] in dic:
                # dic may == 0
                if dic[s[end]] > 0:
                    score += 1
                dic[s[end]] -= 1
            end += 1
            while score == len(t):
                if minLength >= end - start:
                    minLength = end - start
                    ans = s[start:end]
                # left
                if s[start] in dic:
                    dic[s[start]] += 1
                    if dic[s[start]] > 0:
                        score -= 1
                start += 1
        return ans


s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minWindow(s, t))
