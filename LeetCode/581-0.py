'''
# Code Explain:
Brute
- Time complexity: O(NlogN)
- Space complexity: O(1)

Two Pointers
- Time complexity: O(N)
- Space complexity: O(1)

Two Stacks
- Time complexity: O(N)
- Space complexity: O(1)
'''

from typing import List


class Solution:
    # sort then find the start and end of sub arr
    def findUnsortedSubarray_brute(self, nums: List[int]) -> int:
        nums2 = sorted(nums)
        l, r = 0, len(nums) - 1
        findL, findR = False, False

        while l <= r:
            if nums[l] == nums2[l]:
                l += 1
            else:
                findL = True
            if nums[r] == nums2[r]:
                r -= 1
            else:
                findR = True

            if findL and findR:
                break

        if findL and findR:
            return r - l + 1
        else:
            return 0

    # Two Pointers
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0

        l, r = 0, len(nums) - 1

        while l < len(nums) - 1 and nums[l] <= nums[l + 1]:
            l += 1

        while r > 0 and nums[r] >= nums[r - 1]:
            r -= 1

        if l > r:
            return 0

        # to reduce space complexity
        # subRange = nums[l:r + 1]
        # rangeMin = min(subRange)
        # rangeMax = max(subRange)
        rangeMin, rangeMax = float('inf'), -float('inf')
        for i in range(l, r + 1):
            rangeMin = min(rangeMin, nums[i])
            rangeMax = max(rangeMax, nums[i])

        while l > 0 and rangeMin < nums[l - 1]:
            l -= 1

        while r < len(nums) - 1 and rangeMax > nums[r + 1]:
            r += 1

        return r - l + 1

    # Two Stacks
    # Asc stack: get the pop element
    # Desc stack: get the pop element
    def findUnsortedSubarray_2(self, nums: List[int]) -> int:
        l, r = float('inf'), -float('inf')
        AscStack = []
        for i in range(len(nums)):
            # The popped elements are all out-of-order elements, 
            # and the smallest index is the left boundary of the out-of-order subarray
            while AscStack and nums[AscStack[-1]] > nums[i]:
                l = min(l, AscStack.pop())
            AscStack.append(i)

        DescStack = []
        for i in reversed(range(len(nums))):
            # The popped elements are all out-of-order elements, 
            # and the smallest index is the left boundary of the out-of-order subarray
            while DescStack and nums[DescStack[-1]] < nums[i]:
                r = max(r, DescStack.pop())
            DescStack.append(i)

        if l == float('inf') and r == -float('inf'):
            return 0
        else:
            return r - l + 1
