'''
Determine if left or right part of arr is in Asc order

nums = left sorted + right sorted

case:
nums = [3, 4, 5, 1, 2]
     L  m        R

check if nums[m] >= nums[L]:
    search right
else:
    search left
'''

class Solution:
    def findMin(self, nums):
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
