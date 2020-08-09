'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

Power set is all possible combinations of all possible lengths, from 0 to n

Backtracking is an algorithm for finding all solutions by exploring all potential candidates
If the solution candidate turns to be not a solution (or at least not the last one), backtracking algorithm discards it by making some changes on the previous step, i.e. backtracks and then try again

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(ans, nums, index, curr):
            # if the combination is done
            if len(curr) == k:  
                ans.append(curr[:])
            for i in range(index, len(nums)):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(ans, nums, i+1, curr)
                # backtrack
                curr.pop()
        
        ans = []
        for k in range(len(nums) + 1):
            backtrack(ans, nums, 0, [])
        return ans


    def subsets_2(self, nums):
        def backtrack(ans, nums, index, curr):
            ans.append(curr)
            [
                backtrack(ans, nums, i+1, curr+[nums[i]])
                for i in range(index, len(nums))
            ]

        ans = []
        backtrack(ans, nums, 0, [])
        return ans


# inputs
IN = [
    ([1, 2, 3]), 
    ([1, 2, 3, 4])
]
useSet = 1
print(Solution().subsets(IN[useSet]))

