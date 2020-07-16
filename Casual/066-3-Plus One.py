# https://leetcode-cn.com/problems/plus-one/


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits) - 1 - i))
        return [int(i) for i in str(num + 1)]


# digits = [1, 2, 3]
digits = [9, 9, 9]
print(Solution().plusOne(digits))
