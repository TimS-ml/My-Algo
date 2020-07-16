# https://leetcode-cn.com/problems/two-sum/
# samilar version, add target - value in dict rather than value


class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                return [d[nums[i]], i]
            else:
                d[target - nums[i]] = i


# nums, target
IN = [([11, 2, 15, 7], 19), ([2, 7, 11, 15], 9), ([3, 2, 4], 6)]
useSet = 2
print(Solution().twoSum(IN[useSet][0], IN[useSet][1]))
