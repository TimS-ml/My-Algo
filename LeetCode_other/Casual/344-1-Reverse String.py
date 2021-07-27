# https://leetcode-cn.com/problems/reverse-string/


class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        L = len(s)
        for i in range(int(L / 2)):
            s[i], s[L - i - 1] = s[L - i - 1], s[i]
        return s


s = ["h", "e", "l", "l", "o"]
# s = []
print(Solution().reverseString(s))
