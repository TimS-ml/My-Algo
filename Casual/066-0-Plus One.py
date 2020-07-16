# https://leetcode-cn.com/problems/plus-one/


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        str_dig = ''.join(str(i) for i in digits)
        str_dig = int(str_dig) + 1
        ans = list(str(str_dig))
        return [int(i) for i in ans]


# digits = [1, 2, 3]
digits = [9, 9, 9]
print(Solution().plusOne(digits))
