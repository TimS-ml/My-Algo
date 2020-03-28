# https://leetcode-cn.com/problems/two-sum/


from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target - nums[i] in nums and nums.index(target - nums[i]) != i:
                return [i, nums.index(target - nums[i])]


# nums, target
IN = [([11, 2, 15, 7], 19), ([2, 7, 11, 15], 9), ([3, 2, 4], 6)]
useSet = 2
print(Solution().twoSum(IN[useSet][0], IN[useSet][1]))
