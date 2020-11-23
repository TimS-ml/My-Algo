'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        for i in range(len(height)):
            max_left, max_right = 0,0
            for j in range(0,i):
                max_left = max(max_left,height[j])
            for j in range(i,len(height)):
                max_right = max(max_right,height[j])
            if min(max_left,max_right) > height[i]:
                ans += min(max_left,max_right) - height[i]

        return ans
