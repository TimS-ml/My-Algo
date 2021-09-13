'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:

'''


class Solution:
    def makesquare_backtrack(self, nums: List[int]) -> bool:
        if len(nums) < 4 or sum(nums) % 4 != 0:
            return False
        nums.sort(reverse=True)
        target = [sum(nums) // 4] * 4
        
        def dfs(idx):
            if idx == len(nums):
                return True
            for i in range(4):
                if nums[idx] <= target[i]:
                    target[i] -= nums[idx]
                    if dfs(idx + 1):
                        return True
                    target[i] += nums[idx]
                else:
                    continue
            return False

        return dfs(0)
