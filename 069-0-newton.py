'''
# Code Explain:
- Time complexity: O(1)
- Space complexity: O(log N)

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''


class Solution:
    # Newton
    def mySqrt(self, x: int) -> int:
        ans = x
        while ans**2 > x:
            ans = int(
                (ans + x / ans) /
                2)  # If there is no int(), it will enter an infinite loop
        return ans

    # Time limit exceeded
    def mySqrt_1(self, x: int) -> int:
        if 0 < x < 4:
            return 1
        if x == 0:
            return 0
        l = int(x / 2) + 2
        for i in range(2, l):
            if i**2 == x:
                return i
            elif i**2 > x:
                return i - 1

    # Small improvement (binary search)
    # Space: O(1)
    # Time: O(log x)
    def mySqrt_2(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = l + (r - l) // 2
            if mid**2 > x:
                r = mid - 1
            elif mid**2 < x:
                l = mid + 1
            else:
                return mid
        return r


# inputs
IN = [(5), (1383856179)]
useSet = 0
print(Solution().mySqrt(IN[useSet]))
