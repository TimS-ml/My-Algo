'''
# Code Explain:
- Time complexity: O(N^3)
- Space complexity: O()

brute force first number + 3sum
'''

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        def threeSum(nums, start, target):
            def twoSumTarget(nums, start, target):
                lo, hi = start, len(nums) - 1
                ans = []
                while lo < hi:
                    s = nums[lo] + nums[hi]
                    left = nums[lo]
                    right = nums[hi]
                    if s < target:
                        while lo < hi and nums[lo] == left:
                            lo += 1
                    elif s > target:
                        while lo < hi and nums[hi] == right:
                            hi -= 1
                    else:
                        ans.append([left, right])
                        while lo < hi and nums[lo] == left:
                            lo += 1
                        while lo < hi and nums[hi] == right:
                            hi -= 1
                return ans
            
            ans = []
            i = start
            while i < len(nums):
                tuples = twoSumTarget(nums, i + 1, target - nums[i])
                for subList in tuples:
                    subList.append(nums[i])
                    ans.append(subList)
                while i < len(nums) - 1 and nums[i] == nums[i+1]:
                    i += 1
                i += 1 

            return ans

        ans = []
        i = 0
        while i < len(nums):
            tuples = threeSum(nums, i + 1, target - nums[i])
            for subList in tuples:
                subList.append(nums[i])
                ans.append(subList)
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
            i += 1 

        return ans
