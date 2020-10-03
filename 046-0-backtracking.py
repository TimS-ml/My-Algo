'''
# Code Explain:
- Time complexity: O(N * N!)
- Space complexity: O(N)

# Pros and Cons:
## Pros:

## Cons:

# Notation:
LC077 / 078
'''


class Solution:
    # this is not universal solution
    def permute(self, nums):
        def backtrack(start):
            if start == n:
                ans.append(nums[:])
            for i in range(start, n):
                # place i-th integer start
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        n = len(nums)
        ans = []
        backtrack(0)
        return ans

    def permute2(self, nums):
        def backtrack(subset):
            if len(nums) == len(subset):
                ans.append(subset[:])
                return
            for i in range(len(nums)):
                if nums[i] in subset:
                    continue
                subset.append(nums[i])
                backtrack(subset)
                subset.pop()

        ans = []
        backtrack([])
        return ans

    # yet another way to avoid duplicate
    def permute3(self, nums):
        def backtrack(subset, nums):
            if not nums:
                ans.append(subset[:])
                return
            for i in range(len(nums)):
                subset.append(nums[i])
                print(nums[:i], nums[i+1:])
                backtrack(subset, nums[:i] + nums[i+1:])
                subset.pop()

        ans = []
        backtrack([], nums)
        return ans

nums = [1, 2, 3]
print(Solution().permute3(nums))
