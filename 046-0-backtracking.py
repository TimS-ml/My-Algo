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
    def permute(self, nums):
        def backtrack(first=0):
            if first == n:
                ans.append(nums[:])
            for i in range(first, n):
                # place i-th integer first
                nums[first], nums[i] = nums[i], nums[first]
                print('before', nums, first, i)
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
                print('after', nums, first, i)

        n = len(nums)
        ans = []
        backtrack()
        return ans


nums = [1, 2, 3]
print(Solution().permute(nums))
