'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(1)

We can calculate plus one outself
We need to storage the carry

# Pros and Cons:
## Pros:
- This should be faster

## Cons:

# Notation:

'''


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
            digits[i] = digit
        if carry == 1:  # if input is 999, after reverse is 000
            return [1] + digits
        return digits


# digits = [1, 2, 3]
digits = [9, 9, 9]
print(Solution().plusOne(digits))
