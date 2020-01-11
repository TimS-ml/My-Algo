# https://leetcode-cn.com/problems/minimum-size-subarray-sum/
# https://leetcode-cn.com/problems/minimum-size-subarray-sum/solution/chang-du-zui-xiao-de-zi-shu-zu-by-leetcode/


class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        if not nums:
            return 0
        l, r = 0, 0
        ans = len(nums) + 1
        res = 0
        # find all possible solutions
        while r < len(nums):
            res += nums[r]
            r += 1
            # when sum(res) in window >= s
            while res >= s:
                ans = min(ans, r-l)
                res -= nums[l]
                l += 1  # left side move right
        return 0 if ans == len(nums) + 1 else ans


s = 7
nums = [2, 3, 1, 2, 4, 3]
print(Solution().minSubArrayLen(s, nums))
