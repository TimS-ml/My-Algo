# https://leetcode-cn.com/problems/plus-one/


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sdigits = str("".join(map(str, digits)))
        # print(sdigits)
        sdigits = int(sdigits) + 1
        ans = list(str(sdigits))
        return ans


# digits = [1, 2, 3]
digits = [9, 9, 9]
print(Solution().plusOne(digits))
