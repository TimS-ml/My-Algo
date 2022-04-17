'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

- reverse, reverse, reverse !!!
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

    def thousandSeparator_2(self, n: int) -> str:
        s = str(n)
        s = s[::-1]
        res = '.'.join(s[i:i + 3] for i in range(0, len(s), 3))
        return res[::-1]

print(Solution().thousandSeparator(1234))
