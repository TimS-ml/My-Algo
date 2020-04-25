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
        str_dig = functools.reduce(lambda total, d: 10 * total + d, digits)
        str_dig = int(str_dig) + 1
        ans = list(str(str_dig))
        return [int(i) for i in ans]


# digits = [1, 2, 3]
digits = [9, 9, 9]
print(Solution().plusOne(digits))
