# https://leetcode-cn.com/problems/palindrome-number/


class Solution:
    def isPalindrome(self, x) -> bool:
        if x >= 0:
            ans = int(str(x)[::-1])
            if ans == x:
                return True
            else:
                return False
        return False


x = 10
print(Solution().isPalindrome(x))