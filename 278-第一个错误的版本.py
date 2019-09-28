# https://leetcode-cn.com/problems/first-ba

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo = 1
        hi = n
        while lo < hi:
            mid = lo + (hi - lo) / 2
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1
        return int(lo)