'''
lc 680
'''

import unittest

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                sl = s[l+1:r+1]
                sr = s[l:r]
                return sl == sl[::-1] or \
                        sr == sr[::-1]

        return True


testFunc = Solution().validPalindrome
class Test(unittest.TestCase):
    def test_dege(self):
        self.assertEqual(testFunc(""), True)

    def test_valid(self):
        self.assertEqual(testFunc("a"), True)
        self.assertEqual(testFunc("aaa"), True)

    def test_valid_after_Del(self):
        self.assertEqual(testFunc("abobca"), True)
        self.assertEqual(testFunc("abab"), True)
        self.assertEqual(testFunc("abc"), False)


if __name__ == '__main__':
    unittest.main()

