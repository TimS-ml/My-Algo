'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

include num + alpha, then lower
'''


class Solution:
    # without mod the string
    def isPalindrome(self, s) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    # mod the string
    def isPalindrome_2(self, s) -> bool:
        # same
        # s = ''.join(filter(str.isalnum, s)).lower()
        s = filter(lambda x: x.isalnum(), s)
        s = map(lambda x: x.lower(), s)
        s = list(s)
        return s == s[::-1]

s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))
