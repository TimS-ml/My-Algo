# https://leetcode-cn.com/problems/maximum-subarray/
# https://www.jianshu.com/p/3ceb0ab8a7be

# 具体思路是，选定一点把数列一分为二，那么最大自数列的值就是从三个值里面选。
# 1）左边子数列中的最大值
# 2）右边子数列中的最大值
# 3）以选定点开始，向两边相加，和的最大值


class Solution:
    def maxSubArray(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            self.maxSubArray(nums[0: len(nums)//2])
            self.maxSubArray(nums[len(nums)//2: len(nums)])
        
        leftMax = nums[len(nums)//2-1]
        tmp = 0
        # for i in range(len(nums)//2-1, -1, -1):
        for i in range(0, len(nums)//2):
            tmp += nums[i]
            leftMax = max(tmp, leftMax)

        rightMax = nums[len(nums)//2]
        tmp = 0
        for i in range(len(nums)//2, len(nums)):
            tmp += nums[i]
            rightMax = max(tmp, rightMax)

        return max(rightMax, leftMax, leftMax+rightMax)


nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums2 = [-2, -3, -1]  # should be -1
print(Solution().maxSubArray(nums2))
