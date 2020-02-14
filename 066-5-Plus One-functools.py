# https://leetcode-cn.com/problems/plus-one/
# https://docs.python.org/3/library/functools.html
# https://en.wikipedia.org/wiki/Horner%27s_method
# this is the fastest solution so far
import functools


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sdigits = functools.reduce(lambda total, d: 10 * total + d, digits, 0)
        # print(sdigits)
        sdigits = int(sdigits) + 1
        ans = list(str(sdigits))
        return ans


# digits = [1, 2, 3]
digits = [9, 9, 9]
print(Solution().plusOne(digits))
