# https://leetcode-cn.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = r = 0
        n = len(s)
        for i in range(n - 1):
            # terminate
            if 2 * (n - i) + 1 < r - l + 1:
                break
            # init
            l = r = i
            # aba
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            # weird boundary
            if r - l - 2 > r - l:
                l = l + 1
                r = r - 1
            l = i
            r = i + 1
            # abba
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 2 > r - l:
                l = l + 1
                r = r - 1
        return s[l:r + 1]
