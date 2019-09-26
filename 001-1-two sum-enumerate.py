# https://leetcode-cn.com/problems/two-sum/submissions/


class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for key, value in enumerate(nums):
            if target - value in d:
                # (target - value)是value
                # d[target - value]返回key
                return [d[target - value], key]
            d[value] = key  # 向前检索
            print(d)


nums = [11, 2, 15, 7]
target = 19

print(Solution().twoSum(nums, target))

