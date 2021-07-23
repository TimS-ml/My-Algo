'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(1)

# Pros and Cons and Notation:
case: abca <-> acba

- 2 types of palindrome:
  - len // 2 == 0 or == 1
- if unmatch:
    - subarr[1:] or subarr[:-1] should be palindrome

'''


class Solution():
    def validPalindrome(self, s):
        l = len(s)
        h = l // 2
        if s[:h] == s[-1:-1 - h:-1]:
            return True

        for i in range(h):
            # unmatch
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                h = (j - i) // 2
                return s[i:i + h] == s[j - 1:j - h - 1:-1] or \
                       s[i + 1:i + h + 1] == s[j:j - h:-1]

    def validPalindrome_2(self, s: str) -> bool:
        def checkPalindrome(low, high):
            i, j = low, high
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return checkPalindrome(low + 1, high) or \
                       checkPalindrome(low, high - 1)
        return True


s = "abobca"
print(Solution().validPalindrome_2(s))
