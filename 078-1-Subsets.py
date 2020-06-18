# https://leetcode-cn.com/problems/subsets/


class Solution:
    def subsets(self, nums):
        def dfs(nums, index, path, ans):
            ans.append(path)
            [
                dfs(nums, i + 1, path + [nums[i]], ans)
                for i in range(index, len(nums))
            ]

        ans = []
        dfs(nums, 0, [], ans)
        return ans


nums = [1, 2, 3]
print(Solution().subsets(nums))
