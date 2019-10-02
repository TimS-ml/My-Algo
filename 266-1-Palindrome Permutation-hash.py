# https://leetcode-cn.com/problems/palindrome-permutation/


class Solution:
    def canPermutePalindrome(self, s):
        calc = {}
        s = list(s)
        for i in s:
            if i in calc:
                calc[i] += 1
            else:
                calc.setdefault(i, 1)
        print(calc)

        once = False
        for i in calc.values():
            if i%2 == 1:
                if once:
                    return False
                once = True
        return True


s = "carerac"
print(Solution().canPermutePalindrome(s))
