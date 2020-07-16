# https://leetcode-cn.com/problems/permutations/
# https://medium.com/algorithms-and-leetcode/backtracking-e001561b9f28


class Solution:
    def permute(self, nums):
        ans = []
        temp = []
        self.backtracking(nums, temp, ans)
        return ans

    def backtracking(self, nums, temp, ans):
        print(temp)
        if len(nums) == len(temp):
            ans.append(list(temp))
        for i in range(len(nums)):
            if nums[i] in temp:
                continue
            temp.append(nums[i])
            self.backtracking(nums, temp, ans)
            # print('depth', len(temp))
            temp.pop()


nums = [1, 2, 3]
print(Solution().permute(nums))
