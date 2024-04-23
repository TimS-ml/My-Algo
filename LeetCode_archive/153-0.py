'''
No dupl

case: ASC arr: [a, b, c, d], rotate: [c, d, a, b]
any number in c~d > any number in a~b

steps:
nums = [3, 4, 5, 1, 2]
        L  m        R

check if nums[m] >= nums[L]:
    search right
else:
    search left
'''

class Solution:
    def findMin(self, nums):
        ans = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                ans = min(ans, nums[l])
                break

            m = (l + r) // 2
            ans = min(ans, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return ans
