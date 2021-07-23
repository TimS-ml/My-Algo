'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:

'''


class Solution():
    def validPalindrome(self, s):
        l = len(s)
        h = l // 2
        if s[:h] == s[-1:-1 - h:-1]: return True

        for i in range(h):
            # unmatch
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                h = (j - i) // 2
                return s[i:i + h] == s[j - 1:j - h - 1:-1] or \
                       s[i + 1:i + h + 1] == s[j:j - h:-1]
