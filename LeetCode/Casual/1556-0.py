'''
# Code Explain:
- Time complexity: O(logn)
- Space complexity: O(logn)


- from right to left
'''


class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        count = 1
        ans = ''
        for i in range(len(n) - 1, -1, -1):
            ans += n[i]
            if count % 3 == 0 and count != len(n):
                ans += '.'
            count += 1
        return ans[::-1]


print(Solution().thousandSeparator(1234))
