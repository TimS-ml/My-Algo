'''
# Code Explain:
- Time complexity: O(C(N,3)) or O(N^3) level
    N choose 3
- Space complexity: O(1)
Pre-process of sorting is in-place, no need of extra space

sol1 
brute force first number + 2sum

sol2
- Time complexity: O(N^2)
Creating a loop to iterate over x, then reduce to two sum with y + z = target = -x
Use 3 pointers more cleverly: i, start, end
- i < start < end
- start + end = target - nums[i]
- the third loop becomes a pointer that starts from the right end of the array and moves to the left
    - we can reduce time complexity to O(N^2)
    - if we find that as the first element increases, the second element decreases, then we can use the two pointers to reduce the time complexity
    - if num[start] increases, then num[end] decreases, related to O(N)

time complexity for num.sort(): O(N logN)

# Notation:
0 <= nums.length <= 3000
'''

from typing import List


class Solution:
    # time O(N^2)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

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
        
        target = 0
        ans = []
        i = 0
        while i < len(nums):
            tuples = twoSumTarget(nums, i + 1, target - nums[i])
            for subList in tuples:
                subList.append(nums[i])
                ans.append(subList)
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
            i += 1 

        return ans
        
    def threeSum_2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        if len(nums) < 3:
            return ans

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = 0 - nums[i]
            start, end = i + 1, len(nums) - 1
            # aggregate two pointers in one loop
            while start < end:
                if nums[start] + nums[end] > target:
                    end -= 1
                elif nums[start] + nums[end] < target:
                    start += 1
                else:
                    ans.append([nums[i], nums[start], nums[end]])
                    # move 2 pointers to avoid duplicate ans
                    # think about case: [-1, 0, 0, 0 , 1, 1]
                    end -= 1
                    start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
        return ans


# inputs
# nums = [-1, 0, 1, 2, -1, -4]
# nums = [-2, 0, 1, 1, 2]
nums = [-1, 0, 0, 0, 1, 1]
print(Solution().threeSum_2(nums))
