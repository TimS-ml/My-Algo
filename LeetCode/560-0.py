'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

input:  [3, 4,  7,  2, -3,  1,  4,  2,  1], K = 7
sum: [0, 3, 7, 14, 16, 13, 14, 18, 20, 21]
     |------|---------------|
                |-----------------------|

same as lc 001, create a dict
- 
- 

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumdict = {0: 1}
        n = len(nums)
        count = 0
        s = 0

        for num in nums:
            print(num, count, sumdict)
            s += num
            if s - k in sumdict:
                count += sumdict[s - k]
            if s in sumdict:
                sumdict[s] += 1  # why ?
            else:
                sumdict[s] = 1
        return count


nums = [3, 4, 7, 2, -3, 1, 4, 2, 1]
k = 7
print(Solution().subarraySum(nums, k))
