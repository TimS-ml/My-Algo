'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

# solution from https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/description/
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        self.best = m * n    
    
        def dfs(height, moves):
            if all(h == n for h in height):
                self.best = min(self.best, moves)
                return
            if moves >= self.best:
                return
            min_height = min(height)
            idx = height.index(min_height)
            ridx = idx + 1
            while ridx < m and height[ridx] == min_height:
                ridx += 1
            for i in range(min(ridx - idx, n - min_height), 0, -1):
                new_height = height[:]
                for j in range(i):
                    new_height[idx + j] += i
                dfs(new_height, moves + 1) 
    
        dfs([0] * m, 0)
        return self.best
