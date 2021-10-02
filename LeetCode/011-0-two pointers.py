'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(1)

# Pros and Cons and Notation:

S(i, j) = min(h[i], h[j]) x (j-i)

- move any boundary, (j-i) will be smaller
- if move smaller boundary, min(h[i], h[j]) might bigger
- if move bigger boundary, min(h[i], h[j]) might not change or smaller
'''


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans
