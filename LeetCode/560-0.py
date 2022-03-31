'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

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
                # to determine the sum of elements for the subarray nums[i:j], 
                #   we can directly use sum[j+1] - sum[i]
                # from above example, if presum = 21, k = 7
                # then the gap between 14(presum-k) and 21 is your target
                # you only need to worry about how many times this 14 apprears
                # attention: add 0 to sum_dict!!!
                ans += sum_dict[presum - k]
            
            sum_dict[presum] = sum_dict.get(presum, 0) + 1
        return ans

    # a very slow brute force solution
    # focus on the edge cases
    # time complexity: O(n^3)
    def subarraySum_2(self, nums: List[int], k: int) -> int:
        ans = 0
        for start in range(len(nums)):
            for end in range(start, len(nums)):
                s = sum(nums[start: end+1])
                if s == k:
                    ans += 1
        return ans

    # presum only, no hash dict
    # time complexity: O(n^2)
    def subarraySum_3(self, nums: List[int], k: int) -> int:
        ans = 0
        for start in range(len(nums)):
            s = 0
            for end in range(start, len(nums)):
                s += nums[end]
                if s == k:
                    ans += 1
        return ans
                
                


nums = [3, 4, 7, 2, -3, 1, 4, 2, 1]
k = 7
print(Solution().subarraySum(nums, k))
