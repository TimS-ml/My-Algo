'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

import math
from typing import List


class Solution(object):
    # two pointers
    def maxSubArray_0(self, nums: List[int]) -> int:
        ans, l, r, curr_sum = nums[0], 0, 1, nums[0]
        while r < len(nums):
            if curr_sum + nums[r] > nums[r]:
                curr_sum += nums[r]
            else:
                l = r
                curr_sum = nums[l]
            ans = max(ans, curr_sum)
            r += 1
        return ans

    # Divide and Conquer
    def maxSubArray_1(self, nums: List[int]) -> int:
        '''
        # 具体思路是, 选定一点把数列一分为二, 那么最大自数列的值就是从三个值里面选.
        # 1)左边子数列中的最大值
        # 2)右边子数列中的最大值
        # 3)以选定点开始, 向两边相加, 和的最大值
        '''

        def findBestSubarray(nums, left, right):
            # Base case - empty array.
            if left > right:
                return -math.inf

            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            # Iterate from the middle to the beginning.
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)

            # Reset curr and iterate from the middle to the end.
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)

            # The best_combined_sum uses the middle element and
            # the best possible sum from each half.
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum

            # Find the best subarray possible from both halves.
            left_half = findBestSubarray(nums, left, mid - 1)
            right_half = findBestSubarray(nums, mid + 1, right)

            # The largest of the 3 is the answer for any given input array.
            return max(best_combined_sum, left_half, right_half)

        # Our helper function is designed to solve this problem for
        # any array - so just call it using the entire input!
        return findBestSubarray(nums, 0, len(nums) - 1)

    # DP
    def maxSubArray_2(self, nums) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [float('-inf') for _ in range(len(nums))]

        dp[0] = nums[0]
        ans = nums[0]
        for each in range(1, len(nums)):
            dp[each] = max(dp[each - 1] + nums[each], nums[each])
            ans = max(ans, dp[each])
        return ans

    # DP rolling optimization
    def maxSubArray_3(self, nums) -> int:
        if len(nums) == 0:
            return 0
        preSum = maxSum = nums[0]
        for i in range(1, len(nums)):
            preSum = max(preSum + nums[i], nums[i])  # 这样有利于找到前n个数里sum最大的
            maxSum = max(maxSum, preSum)
        return maxSum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().maxSubArray_3(nums))
