'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons:
## Pros:

## Cons:

# Notation:
LC077 / 078
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

    def permute(self, nums):
        def backtrack(temp, ans):
            print(temp)
            if len(nums) == len(temp):
                ans.append(list(temp))
            for i in range(len(nums)):
                if nums[i] in temp:
                    continue
                temp.append(nums[i])
                backtrack(temp, ans)
                # print('depth', len(temp))
                temp.pop()

        ans = []
        temp = []
        backtrack(temp, ans)
        return ans

nums = [1, 2, 3]
print(Solution().permute(nums))
