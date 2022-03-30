'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

'''


class Solution:
    def reverseString(self, s) -> None:
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    # Space: O(N)
    def reverseString_2(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def rever(start, end, li):
            if start >= end:
                return li
            li[start], li[end] = li[end], li[start]
            return rever(start + 1, end - 1, li)

        rever(0, len(s) - 1, s)


s = ["h", "e", "l", "l", "o"]
# s = []
print(Solution().reverseString(s))
