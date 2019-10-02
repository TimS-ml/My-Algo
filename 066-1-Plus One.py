# https://leetcode-cn.com/problems/plus-one/


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        
        for i in reversed(range(0, len(digits))):  # 倒着遍历
            # 进位之后可能会出现digit < digits[i]，十位、百位等等可能都需要进位
            digit = (digits[i] + carry) % 10  # 考虑进位，比如digits[i] = 9
            carry = 1 if digit < digits[i] else 0
            # print(digit, carry)
            digits[i] = digit
        if carry == 1:  # 如果输入[999]，遍历到最后是[000]，需要在第一位补"1"
            return [1] + digits
        return digits


# digits = [1, 2, 3]
digits = [9, 9, 9]
print(Solution().plusOne(digits))
