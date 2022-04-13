'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()


[[0,1,1,0,0,0],
 [0,1,0,1,1,0],
 [0,1,1,0,1,0],
 [0,0,0,1,1,0],
 [1,1,1,1,1,0],
 [1,1,1,1,1,0]]

Feedback:
8 directions!!! You only wrote 3 of them
'''

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, g: List[List[int]]) -> int:
        if g[0][0]!=0 or g[-1][-1]!=0:
            return -1
        
        # i, j, path
        q = deque([(0, 0, 1)])

        # (i, j): path
        dic = {}

        n = len(g)-1 # max idx

        while q:
            i, j, path = q.popleft()

            if (i, j) in dic:
                if path >= dic[(i, j)]:
                    continue
                else:
                    dic[(i, j)] = path
            else:
                dic[(i, j)] = path

            if i == n and j == n:
                return dic[(i, j)]

            if i < n and j < n and g[i+1][j+1] == 0:
                q.append((i+1, j+1, path+1))
            if i < n and g[i+1][j] == 0:
                q.append((i+1, j, path+1))
            if j < n and g[i][j+1] == 0:
                q.append((i, j+1, path+1))
        
        if (i, j) in dic:
            return dic[(i, j)]
        else:
            return -1
