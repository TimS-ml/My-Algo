# https://leetcode-cn.com/problems/reverse-string/
# 可以return s[::-1]


class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) - 1
        while start <= end:
            tmp = s[start]
            s[start] = s[end]
            s[end] = tmp
            start += 1
            end -= 1
        return s


# s = ["h", "e", "l", "l", "o"]
s = []
print(Solution().reverseString(s))
