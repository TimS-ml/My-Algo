'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

Backtracking and DP also works, but takes longer time
'''

class Solution:
    def canJump(self, nums) -> bool:
        n = len(nums)
        last_position = n - 1
        for i in range(n - 1, -1, -1):
            # can reach the last position
            # ... 3, 0, 1 ...
            #  i+3 > last_position (at 1, at which can reach to the end)
            if (nums[i] + i) >= last_position:
                last_position = i
        return last_position == 0

    def canJump_2(self, nums) -> bool:
        start = 0
        end = 0
        while start <= end and end < len(nums) - 1:
            end = max(end, nums[start] + start)
            start += 1
        return end >= len(nums) - 1


nums1 = [2, 3, 1, 1, 4]
nums2 = [3, 2, 1, 0, 4]
nums3 = [2, 4, 2, 1, 0, 2, 0]
print(Solution().canJump(nums3))
