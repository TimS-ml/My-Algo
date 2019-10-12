# https://leetcode-cn.com/problems/palindrome-permutation/

import collections


class Solution:
    def canPermutePalindrome(self, s):
        calc = dict(collections.Counter(s))
        print(calc)
        once = False
        for i in calc.values():
            if i % 2 == 1:
                if once:
                    return False
                once = True
        return True


s = "carerac"
print(Solution().canPermutePalindrome(s))
