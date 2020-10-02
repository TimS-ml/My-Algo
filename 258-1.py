'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

There is a known formula to compute a digital root in a decimal numeral system
https://brilliant.org/wiki/digital-root/

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''


class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # if num == 0:
        #     return 0
        # if num % 9 == 0:
        #     return 9
        # return num % 9

        return 1 + (num - 1) % 9 if num else 0

    def addDigits_2(self, num):
        """
        :type num: int
        :rtype: int
        """
        while (num >= 10):
            temp = 0
            while (num > 0):
                temp += num % 10
                num /= 10
            num = temp
        return num


# inputs
IN = [(38), (128)]
useSet = 1
print(Solution().addDigits(IN[useSet]))
