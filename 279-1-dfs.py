'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''

class Solution:
    def numSquares(self, n: int) -> int:
        # Generate the squares, reverse to be in decreasing order for efficiency.
        sqrs = [i**2 for i in range(1, int(math.sqrt(n))+1)][::-1]
        mins = float('inf')
        
        def helper(start, subset, number):
            nonlocal mins
            l = len(subset)
            # If the current subset we're using >= the min that lead to the target return.
            # If number < 0 or > n return.
            if l >= mins or number < 0 or number > n:
                return
            # If by this stage our number == 0 we store the l, this only gets update if l < mins.
            if number == 0:
                mins = l
                return
            else:
                # Recursively work through the sqrs.
                for i in range(start, len(sqrs)):
                    helper(i, subset + [sqrs[i]], number - sqrs[i])
        
        helper(0, [], n)
        return mins if mins != float('inf') else -1

