# https://leetcode-cn.com/problems/permutations/


class Solution:
    def permute(self, nums):
        ans = []
        temp = []
        self.backtracking(nums, temp, ans)
        return ans

    def backtracking(self, nums, temp, ans):
        if len(nums) == len(temp):
            ans.append(list(temp))
        for i in range(len(nums)):
            if nums[i] in temp:
                continue
            temp.append(nums[i])
            self.backtracking(nums, temp, ans)
            temp.pop()


nums = [1, 2, 3]
print(Solution().permute(nums))
