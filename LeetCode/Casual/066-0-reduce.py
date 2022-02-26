'''
# Code Explain:
- Time complexity: O(n)
    since we need to go through the list
- Space complexity: O(1)

The intuitive way is to convert to a string and convert back
Here, I provide 4 methods

# Pros and Cons:
## Pros:
- No need to worry about special circumstances

## Cons:
- Need to convert several times

# Notation:
We can only join a str list
We need to return a int list, not a str list

'''


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        str_dig = ''.join(str(i) for i in digits)

        # str_dig = sum(d * (10**i) for i, d in enumerate(digits[::-1]))

        # str_dig = 0
        # for i in range(len(digits)):
        #     str_dig += digits[i] * pow(10, (len(digits) - 1 - i))

        # str_dig = functools.reduce(lambda total, d: 10 * total + d, digits)

        str_dig = int(str_dig) + 1

        ans = list(str(str_dig))
        return [int(i) for i in ans]


# digits
IN = [([1, 2, 5, 7]), ([9, 9, 9])]
useSet = 1
print(Solution().plusOne(IN[useSet]))
