'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

if brute force, O(N^2)

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): 
            return -1
        start, agg = 0, 0
        for i in range(len(gas)):
            agg += gas[i] - cost[i]
            if agg < 0:
                start, agg = i+1, 0
        return start
