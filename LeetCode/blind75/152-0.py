class Solution:
    '''
    [-2,3,-4]
    [2,-5,-2,-4,3]
    '''
    def maxProduct_wrong(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]

        dp1 = [0] * (len(nums) + 1)
        dp1[1] = nums[0]

        dp2 = [0] * (len(nums) + 1)
        dp2[1] = nums[0]

        for i in range(2, len(nums) + 1):
            dp1[i] = max(nums[i-1], nums[i-1] * dp1[i-1])
            if abs(nums[i-1]) > abs(nums[i-1] * dp2[i-1]):
                dp2[i] = nums[i-1]
            else:
                dp2[i] = nums[i-1] * dp2[i-1]

        return max(max(dp1), max(dp2))

    # DP, but no dp table, only min and max val
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)
            max_so_far = temp_max
            result = max(max_so_far, result)

        return result
