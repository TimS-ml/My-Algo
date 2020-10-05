'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons:
## Pros:

## Cons:

# Notation:
remember to sort !!!
LC046: no duplication version
'''

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def backtrack(subset, nums):
            if not nums:
                ans.append(subset[:])
                return
            for i in range(len(nums)):
                if i > 0 and nums[i - 1] == nums[i]:
                    continue
                subset.append(nums[i])
                # print('sub:{} {}, nums:{}, i:{}'.format(nums[:i], nums[i+1:], nums, i))
                backtrack(subset, nums[:i] + nums[i + 1:])
                subset.pop()

        ans = []
        backtrack([], nums)
        return ans

    # create a list to track if visited or not
    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        used = [False for i in nums]

        def backtrack(subset, nums, used):
            if len(subset) == len(nums):
                ans.append(list(subset))
            for i in range(len(nums)):
                if used[i] or i > 0 and nums[i] == nums[i -
                                                        1] and not used[i - 1]:
                    continue
                subset.append(nums[i])
                used[i] = True  # track visit
                backtrack(subset, nums, used)
                used[i] = False
                subset.pop()

        ans = []
        backtrack([], nums, used)
        return ans


nums = [1, 1, 2]
print(Solution().permuteUnique2(nums))
