'''
# Code Explain:
- Time complexity: O(C(N,3)) or O(N^3) level
    N choose 3
- Space complexity: O(1)
Pre-process of sorting is in-place, no need of extra space

sol1 
brute force:
- go through all possibilities
- need 3 pointers to do that

sol2
Creating a loop to iterate over x, then reduce to two sum with y + z = target = -x
Use 3 pointers more cleverly: i, start, end
- i < start < end
- start + end = target - nums[i]
- the third loop becomes a pointer that starts from the right end of the array and moves to the left
    - we can reduce time complexity to O(N^2)
    - if we find that as the first element increases, the second element decreases, then we can use the two pointers to reduce the time complexity
    - if num[start] increases, then num[end] decreases, related to O(N)

time complexity for num.sort(): O(N longN)


# Pros and Cons:
## Pros:

## Cons:
- The trade-off of sort cost us O(N logN), in this case we can ignore that


# Notation:

'''

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0 and [nums[i], nums[j], nums[k]] not in ans:
                        ans.append([nums[i], nums[j], nums[k]])
        return ans


    def threeSum_2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            start, end = i+1, len(nums)-1
            # aggregate two pointers in one loop
            while start < end:
                if nums[start] + nums[end] > target:
                    end -= 1
                elif nums[start] + nums[end] < target:
                    start += 1
                else:
                    ans.append([nums[i], nums[start], nums[end]])
                    end -= 1
                    start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
        return ans


# inputs
IN = [
    ([-1, 0, 1, 2, -1, -4]), 
    ([-2, 0, 1, 1, 2])
]
useSet = 0
print(Solution().threeSum_2(IN[useSet]))

