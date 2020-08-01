'''
# Code Explain:
- Time complexity: O(C(n,k))
    n choose 3
- Space complexity: O()

brute force
- go through all possibilities
- need 3 pointers to do that

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0 and [nums[i], nums[j], nums[k]] not in ans:
                        ans.append([nums[i], nums[j], nums[k]])
        return ans


# inputs
IN = [
    ([-1, 0, 1, 2, -1, -4]), 
    ([1, 2, 3])
]
useSet = 0
print(Solution().threeSum(IN[useSet]))

