'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

Union find in 1d
usually 

for i in range(row):
    for j in range(col):
        index = i*col + j
'''

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0: return 0
        row = len(grid); col = len(grid[0])

        # init ans
        self.count = sum(grid[i][j]=='1' for i in range(row) for j in range(col))
        parent = [i for i in range(row*col)]  # groupTag
        
        def find(x):
            if parent[x]!= x:
                return find(parent[x])
            return parent[x]
        
        def union(x, y):
            xroot, yroot = find(x), find(y)
            if xroot == yroot:
                return 
            parent[xroot] = yroot
            self.count -= 1
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    continue
                index = i*col + j
                if j < col-1 and grid[i][j+1] == '1':
                    union(index, index+1)
                if i < row-1 and grid[i+1][j] == '1':
                    union(index, index+col)

        return self.count


class Solution_2(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # TIME O(MN)
        # SPACE O(MN)
    
        if not grid or not len(grid) or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])

        # two dimension to one
        groupTag = [0 for i in range(m*n)]

        # init groupTag val
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    groupTag[i*n+j] = i*n + j
                else:
                    groupTag[i*n+j] = -1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                if j+1 < n and grid[i][j+1] == '1':
                    self.union(i,j,i,j+1,groupTag,n)
                if i+1 < m and grid[i+1][j] == '1':
                    self.union(i,j,i+1,j,groupTag,n)
        
        count = 0
        for i in range(len(groupTag)):
            if groupTag[i] == i:
                count += 1
        return count
        
    def find(self, e, groupTag):
        # isolate
        if groupTag[e] == e:
            return e
        # group
        else:
            return self.find(groupTag[e], groupTag)
    
    # in this example, x y is i j move 1
    def union(self, i, j, x, y, groupTag, n):
        index1 = i*n+j
        index2 = x*n+y
        root1 = self.find(index1, groupTag)
        root2 = self.find(index2, groupTag)
        # already unioned
        if root1 == root2:
            return
        else:
            groupTag[root2] = root1


class UF:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.n = n
        self.size = n  # init ans

    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi != pj:
            self.size -= 1
            self.p[pj] = pi

    def find(self, i):
        if i != self.p[i]:
            self.p[i] = self.find(self.p[i])
        return self.p[i]


class Solution_3:
    def numIslands(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        d = dict()
        idx = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    d[i, j] = idx
                    idx += 1

        uf = UF(idx)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    if i > 0 and grid[i-1][j] == '1':
                        uf.union(d[i-1, j], d[i, j])
                    if j > 0 and grid[i][j-1] == '1':
                        uf.union(d[i, j-1], d[i, j])
        return uf.size
