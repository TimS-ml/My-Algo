# https://leetcode-cn.com/problems/two-sum/


class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for key, value in enumerate(nums):
            if target - value in d:
                return [d[target - value], key]
            d[value] = key


# nums, target
IN = [([11, 2, 15, 7], 19), ([2, 7, 11, 15], 9), ([3, 2, 4], 6)]
useSet = 2
print(Solution().twoSum(IN[useSet][0], IN[useSet][1]))
