'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

input:     [3, 4,  7,  2, -3,  1,  4,  2,  1], K = 7
presum: [0, 3, 7, 14, 16, 13, 14, 18, 20, 21]
        |------|---------------|
                   |-----------------------|

same as lc 001, create a count dict on presum
'''

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_dict = {0: 1}  # a count dict
        ans = 0
        presum = 0

        for num in nums:
            presum += num

            if presum - k in sum_dict:
                # from above example, if presum = 21, k = 7
                # then the gap between 14(presum-k) and 21 is your target
                # you only need to worry about how many times this 14 apprears
                # attention: add 0 to sum_dict!!!
                ans += sum_dict[presum - k]
            
            sum_dict[presum] = sum_dict.get(persum, 0) + 1
        return ans


nums = [3, 4, 7, 2, -3, 1, 4, 2, 1]
k = 7
print(Solution().subarraySum(nums, k))
