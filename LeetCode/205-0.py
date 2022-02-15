'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(1)


- freq dict is the same
- position is the same

Any one character of s is uniquely corresponding to t, and a single character of t is corresponding to the only character in s
This is also known as the "bijective" relationship

check lc 290
for case
s = "bbbaaaba"
t = "aaabbbba"
2 chars, 4 patterns
'''


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = {}
        t2s = {}
        for i in range(len(s)):
            if (s[i] in s2t and s2t[s[i]] != t[i]) or \
               (t[i] in t2s and t2s[t[i]] != s[i]):
                return False
            s2t[s[i]] = t[i]
            t2s[t[i]] = s[i]
        return True

    def isIsomorphic_2(self, s: str, t: str) -> bool:
        s_li = list(s)
        t_li = list(t)
        pattern = zip(s_li, t_li)
        return len(set(pattern)) == len(set(s_li)) == len(set(t_li))

    def isIsomorphic_3(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            if s.index(s[i]) != t.index(t[i]):
                return False
        return True


s = "bbbaaaba"
t = "aaabbbba"
print(Solution().isIsomorphic(s, t))
print(Solution().isIsomorphic_2(s, t))
