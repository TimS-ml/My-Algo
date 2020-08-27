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

