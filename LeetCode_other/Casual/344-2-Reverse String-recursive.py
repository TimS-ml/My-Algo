# https://leetcode-cn.com/problems/reverse-string/
# this is not in-place, but good one


class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        L = len(s)
        if L < 2:
            return s
        return self.reverseString(s[int(L / 2):]) + self.reverseString(
            s[:int(L / 2)])


s = ["h", "e", "l", "l", "o"]
# s = []
print(Solution().reverseString(s))
