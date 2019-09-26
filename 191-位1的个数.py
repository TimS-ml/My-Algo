# https://leetcode-cn.com/problems/number-of-1-bits/

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n > 0:
            n -= (n & -n)  # bit
            ans += 1
        return ans


inpute = '00000000000000000000000000001011'
n = int(inpute)
print(n)
print(Solution().hammingWeight(n))
