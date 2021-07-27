# https://leetcode-cn.com/problems/maximum-subarray/
# https://www.jianshu.com/p/3ceb0ab8a7be

# 具体思路是，选定一点把数列一分为二，那么最大自数列的值就是从三个值里面选。
# 1）左边子数列中的最大值
# 2）右边子数列中的最大值
# 3）以选定点开始，向两边相加，和的最大值


class Solution:
    def maxSubArray(self, nums) -> int:
        return Solution().recursion(nums, len(nums) // 2, 0, len(nums) - 1)

    def recursion(self, nums, base, leftLimit, rightLimit):
        # 设定边界
        leftMax = nums[leftLimit]
        rightMax = nums[rightLimit]
        maxSum = base

        if (base - leftLimit <= 1) and (rightLimit - base <= 1):
            maxSum = max(maxSum, leftMax, rightMax)
            return maxSum

        leftSum = 0
        for i in range(leftLimit, base + 1, -1):
            leftSum += nums[i]
            leftMax = max(leftMax, leftSum)

        rightSum = 0
        for i in range(base, rightLimit + 1):
            rightSum += nums[i]
            rightMax = max(rightMax, rightSum)

        maxSum = leftMax + rightMax - nums[base]
        searchLeft = Solution().recursion(nums, (leftLimit + base) // 2,
                                          leftLimit, base - 1)
        searchRight = Solution().recursion(nums, (rightLimit + base) // 2,
                                           base + 1, rightLimit)
        maxSum = max(searchLeft, searchRight, maxSum)

        return maxSum


nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums2 = [-2, -3, -1]
print(Solution().maxSubArray(nums2))
