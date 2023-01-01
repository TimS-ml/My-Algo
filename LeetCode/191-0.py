'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

n is int, but we need to count '1' in bit format

'&': only 1 + 1 return 1, else 0

remove last '1' in n
n -= (n & -n)
n = n & (n - 1)
'''


class Solution(object):
    def hammingWeight(self, n):
        ans = 0
        while n > 0:
            n -= (n & -n)
            # n = n & (n - 1)
            ans += 1
        return ans


inpute = '00000000000000000000000000001011'
n = int(inpute)
print(n)
print(Solution().hammingWeight(n))
