# https://leetcode-cn.com/problems/plus-one/


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1

        for i in reversed(range(0, len(digits))):
            # after carry, digit < digits[i]
            digit = (digits[i] + carry) % 10
            carry = 1 if digit < digits[i] else 0
            # print(digit, carry)
            digits[i] = digit
        if carry == 1:  # if input is 999, after reverse is 000
            return [1] + digits
        return digits


# digits = [1, 2, 3]
digits = [9, 9, 9]
print(Solution().plusOne(digits))
