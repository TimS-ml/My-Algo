'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0: return 0
        row = len(grid); col = len(grid[0])
        self.count = sum(grid[i][j]=='1' for i in range(row) for j in range(col))
        parent = [i for i in range(row*col)]
        
        def find(x):
            if parent[x]!= x:
                return find(parent[x])
            return parent[x]
        
        def union(x,y):
            xroot, yroot = find(x),find(y)
            if xroot == yroot: return 
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


class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            self.count -= 1

    def getCount(self):
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

