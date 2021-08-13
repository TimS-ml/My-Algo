'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

# Pros and Cons and Notation:

dp * 2
state: leftMax and rightMax
'''

from typing import List


class Solution:
    # Time: O(N^2)
    def trap_brute(self, height: List[int]) -> int:
        ans = 0
        for i in range(len(height)):
            max_left, max_right = 0, 0
            # find max_left, search repeatedly
            for j in range(0, i):
                max_left = max(max_left, height[j])
            # find max_right, search repeatedly
            for j in range(i, len(height)):
                max_right = max(max_right, height[j])
            if min(max_left, max_right) > height[i]:
                ans += min(max_left, max_right) - height[i]

        return ans

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)

        leftMax = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax = [0] * (n - 1) + [height[n - 1]]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        
        # remember to - height[i]
        ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
        return ans
