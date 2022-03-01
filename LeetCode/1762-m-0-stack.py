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
    def findBuildings(self, heights: List[int]) -> List[int]:
        '''
        Monotonic Stack
        '''
        n = len(heights)
        answer = []
        stack = []
        
        for current in range(n):
            while stack and heights[current] >= stack[-1]:
                stack.pop()
                answer.pop()
            stack.append(heights[current])
            answer.append(current)
        
        return answer

    def findBuildings_2(self, heights: List[int]) -> List[int]:
        '''
        Space Optimization
        '''
        n = len(heights)
        answer = []
        max_height = -1
        
        for current in reversed(range(n)):
            if heights[current] > max_height:
                answer.append(current)
                max_height = heights[current]
        
        answer.reverse()  # remember to reverse it
        return answer
