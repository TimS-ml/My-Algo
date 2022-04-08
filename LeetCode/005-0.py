'''
# Code Explain:
- Time complexity: O(N^2)
- Space complexity: O(1)

Palindrome: two pointers
'''


class Solution:
    def longestPalindromeo(self, s: str) -> str:
        # start at middle, move to the left and right end
        # if same start l, r => find odd len sub str
        # if l + 1 = r, then find even len sub str
        def find_palidrome(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]
        
        ans = ''
        for i in range(len(s)):
            s1 = find_palidrome(s, i, i)  # aba
            s2 = find_palidrome(s, i, i+1)  # abba
            if len(ans) < len(s1):
                ans = s1
            if len(ans) < len(s2):
                ans = s2
        return ans


    def longestPalindromeo_2(self, s: str) -> str:
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
