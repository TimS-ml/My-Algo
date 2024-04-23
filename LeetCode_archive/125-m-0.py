'''
char.isalnum()

s = '12321'

'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:  # odd and even
            while s[l].isalnum() == False and l < r:
                l += 1
            while s[r].isalnum() == False and l < r:
                r -= 1

            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True   # ends at [1] l==r or [2] l > r


    def isPalindrome_2(self, s: str) -> bool:
        s = s.lower()
        s2 = ''
        for c in list(s):
            if c.isalnum():
                s2 += c

        return s2 == s2[::-1]

