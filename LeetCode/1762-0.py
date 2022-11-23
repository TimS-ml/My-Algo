'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

A building has an ocean view if
all the buildings to its right have a smaller (h >= h_right) height.


# Brute force
Time O(n^2)
function tallest(start):
    return tallest building in li[start+1:]

tallest_li = [tallest(li, i) for i in range xxx]
compare if li[i] > tallest_li(i)


# Monotonic Stack
Know ans[-1] = 1


# Loop Reverslly (space optimization)
Loop reverslly, we should ideally found an increasing seq
Just mark the non increasing seq idx
'''

from typing import List

class Solution:
    # Monotonic Stack
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = []
        stack = []

        for i in range(n):
            # building i block some of the building before i
            while stack and heights[i] >= stack[-1]:
                stack.pop()
                ans.pop()
            stack.append(heights[i])
            ans.append(i)

        return ans

    # Space Optimization
    def findBuildings_2(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = []
        max_height = -1

        for i in reversed(range(n)):
            if heights[i] > max_height:
                ans.append(i)
                max_height = heights[i]

        ans.reverse()  # remember to reverse it
        return ans
