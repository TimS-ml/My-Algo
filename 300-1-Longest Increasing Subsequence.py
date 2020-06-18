# https://leetcode-cn.com/problems/longest-increasing-subsequence/
# find the largest end element in tails that is smaller than nums[i]
# and then replace it with nums[i] and discard the list in the same length
# which is implemented by 'tail[idx] = i'

import bisect


class Solution:
    def lengthOfLIS(self, nums) -> int:
        tail = []
        for i in nums:
            # please remember bisect is for sorted list
            # tail[0] will be the minium number in the input
            idx = bisect.bisect_left(tail, i)
            if idx == len(tail):
                tail.append(i)
            else:
                tail[idx] = i
            print(idx, tail)
        return len(tail)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(Solution().lengthOfLIS(nums))
