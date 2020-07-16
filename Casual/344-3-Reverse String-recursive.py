# https://leetcode-cn.com/problems/reverse-string/


class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def rever(start, end, li):
            if start >= end:
                return li
            li[start], li[end] = li[end], li[start]
            return rever(start + 1, end - 1, li)

        rever(0, len(s) - 1, s)
        print(s)


s = ["h", "e", "l", "l", "o"]
# s = []
print(Solution().reverseString(s))
