# https://leetcode-cn.com/problems/palindromic-substrings/


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            # find pattern like 'aca'
            left = right = i
            while left >= 0 and right < n and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1

            # find pattern like 'abba'
            left = i
            right = i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans


s = 'aaa'
print(Solution().countSubstrings(s))
