# https://leetcode-cn.com/problems/subarray-product-less-than-k/


class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            # left stay at the start position of window
            while prod >= k:
                # this is smart
                prod /= nums[left]
                left += 1
                print(prod, left)
            # when r at num[1], l at num[0], ans += 2
            # which are 10*5 and 5
            ans += right - left + 1
            print(prod, left, right, ans)
        return ans


nums = [10, 5, 2, 6]
nums2 = [10, 5, 100, 6]
k = 100
print(Solution().numSubarrayProductLessThanK(nums2, k))
