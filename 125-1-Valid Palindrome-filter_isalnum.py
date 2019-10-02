# https://leetcode-cn.com/problems/valid-palindrome/


class Solution:
    def isPalindrome(self, s) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()  # str.isalnum过滤掉所有的符
        print(s)  # amanaplanacanalpanama
        return s == s[::-1]


s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))