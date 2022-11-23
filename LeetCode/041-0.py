'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

search -> hash set

[1] Build hash set
[2] Starting from assuming missing number = 1
    Search in hash set

The worse case:
[1, 2, 3], missing 4 = len(arr) + 1
solution set = [1, len(arr) + 1], len(sol set) = len(arr)

Memory Optimization:
sol set and input arr mapping
'''

from typing import List


class Solution:
    # from NeetCode, use list as hash set
    def firstMissingPositive(self, nums):
        # set neg num to 0
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        # use list as hash set
        # mimic checking from 1 to len(nums)+1
        # if valid val in nums => save the checking result to idx=val-1 by *= -1
        # case A0 = [2, 1]
        # val = 2, set idx=val-1=1 to *= -1
        #      A1 = [2, -1]
        # then loop to next value, abs(A1[1]) = A0[1], no info loss
        # val = 1, set idx=val-1=0 to *=-1
        #      A2 = [-2, -1]
        # then, check the '-' sing in An
        # if we found a '+' number nums[i], means this i does not exsit in An
        # return this idx
        # the idx i matters, but we don't care about the value of abs(nums[i])
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)

        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        return len(nums) + 1

    # from official, use list as hash set
    def firstMissingPositive_2(self, nums: List[int]) -> int:
        n = len(nums)

        # Base case.
        if 1 not in nums:
            return 1

        # Replace negative numbers, zeros,
        # and numbers larger than n by 1s.
        # After this convertion nums will contain
        # only positive numbers.
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        # Use index as a hash key and number sign as a presence detector.
        # For example, if nums[1] is negative that means that number `1`
        # is present in the array.
        # If nums[2] is positive - number 2 is missing.
        for i in range(n):
            a = abs(nums[i])
            # If you meet number a in the array - change the sign of a-th element.
            # Be careful with duplicates : do it only once.
            if a == n:
                nums[0] = -abs(nums[0])
            else:
                nums[a] = -abs(nums[a])

        # Now the index of the first positive number
        # is equal to first missing positive.
        for i in range(1, n):
            if nums[i] > 0:
                return i

        if nums[0] > 0:
            return n

        return n + 1

    # cyc sort
    # https://leetcode.com/problems/first-missing-positive/discuss/858526/Cyclic-Sort-Explained
    def firstMissingPositive_3(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums):
            if nums[i] > 0 and nums[i] <= len(nums) and \
                    nums[i] != nums[nums[i] - 1]:
                # You cannot direct using x, y = y, x in this case
                a, b = nums[nums[i] - 1], nums[i]
                nums[nums[i] - 1], nums[i] = b, a
                # print(i, nums)
                # import pdb; pdb.set_trace()
            else:
                i += 1

        print(nums)
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1


# nums = [1, 2, 0]
nums = [3, 4, -1, 1]
# nums = [7, 8, 9, 11, 12]
print(Solution().firstMissingPositive_3(nums))
