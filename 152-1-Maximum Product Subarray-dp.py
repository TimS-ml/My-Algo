# https://leetcode-cn.com/problems/maximum-product-subarray/


class Solution:
    def maxProduct(self, nums) -> int:
        maxDP = [0 for _ in range(0, len(nums))]
        minDP = [0 for _ in range(0, len(nums))]
        maxDP[0] = nums[0]
        minDP[0] = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            maxDP[i] = max(minDP[i-1]*nums[i], nums[i], maxDP[i-1]*nums[i])
            minDP[i] = min(minDP[i-1]*nums[i], nums[i], maxDP[i-1]*nums[i])
            # print(maxDP[i], minDP[i])
            print(minDP[i-1]*nums[i], nums[i], maxDP[i-1]*nums[i])
            ans = max(ans, maxDP[i])
        return ans


nums = [2, 3, -2, 4]  # 6
print(Solution().maxProduct(nums))
