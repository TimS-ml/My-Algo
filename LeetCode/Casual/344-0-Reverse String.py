# https://leetcode-cn.com/problems/reverse-string/


class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()


s = ["h", "e", "l", "l", "o"]
# s = []
print(Solution().reverseString(s))
