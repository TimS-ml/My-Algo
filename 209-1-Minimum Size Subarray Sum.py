# https://leetcode-cn.com/problems/minimum-size-subarray-sum/
# https://leetcode-cn.com/problems/minimum-size-subarray-sum/solution/chang-du-zui-xiao-de-zi-shu-zu-by-leetcode/


class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        sum = 0
        j = 0
        ans = float('inf')
        for i in range(0, len(nums)):
            while j < len(nums) and sum < s:
                sum += nums[j]
                j += 1
            if sum >= s:
                ans = min(ans, j - i)
            sum -= nums[i]
            # print(sum)
        return ans if ans != float('inf') else 0


s = 7
nums = [2,3,1,2,4,3]
print(Solution().minSubArrayLen(s, nums))
