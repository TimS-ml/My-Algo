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
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr_neg, max_neg, idx = 0, 0, -1
        for i in range(len(gas)):
            curr_neg += gas[i] - cost[i]
            if max_neg > curr_neg:
                max_neg = curr_neg
                idx = i
            
        return -1 if curr_neg < 0 else idx + 1
