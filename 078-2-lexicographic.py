'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

The idea is that we map each subset to a bitmask of length n, where 1 on the ith position in bitmask means the presence of nums[i] in the subset, and 0 means its absence.

For instance, the bitmask 0..00 (all zeros) corresponds to an empty subset, and the bitmask 1..11 (all ones) corresponds to the entire input array nums.

Hence to solve the initial problem, we just need to generate n bitmasks from 0..00 to 1..11.

# Pros and Cons:
## Pros:

## Cons:
The real problem here is how to deal with zero left padding, because one has to generate bitmasks of fixed length, i.e. 001 and not just 1

```
nth_bit = 1 << n
for i in range(2**n):
    # generate bitmask, from 0..00 to 1..11
    bitmask = bin(i | nth_bit)[3:]
```
or

```
for i in range(2**n, 2**(n + 1)):
    # generate bitmask, from 0..00 to 1..11
    bitmask = bin(i)[3:]
```

# Notation:

'''

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        
        for i in range(2**n, 2**(n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            
            # append subset corresponding to that bitmask
            ans.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        
        return ans

# inputs
IN = [
    ([1, 2, 3]), 
    ([1, 2, 3, 4])
]
useSet = 1
print(Solution().subsets(IN[useSet]))


