'''
# Code Explain:
- Time complexity: O(logn)
- Space complexity: O(1)

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''


class Solution:
    def isPalindrome(self, x) -> bool:
        if x < 0:
            return False
        ans = 0
        number = x
        while x != 0:
            # print(x, ans)
            ans = ans * 10 + x % 10
            x //= 10
        return ans == number

    # If you insistent to use str...
    def isPalindrome2(self, x) -> bool:
        if x >= 0:
            ans = int(str(x)[::-1])
            if ans == x:
                return True
            else:
                return False
        return False


# x = 10
x = 121
print(Solution().isPalindrome(x))
