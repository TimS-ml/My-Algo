# https://leetcode-cn.com/problems/walls-and-gates/


class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        m = len(rooms)
        n = len(rooms[0])
        for i in range(m):
            for j in range(n):
                # start
                if rooms[i][j] == 0:
                    self.dfs(i, j, rooms, 0)

    def dfs(self, r, c, rooms, d):
        if r < 0 or c < 0 or r >= len(rooms) or c >= len(rooms[0]) or rooms[r][c] < d:
            return
        # mark as 0 and then other path + 1
        rooms[r][c] = d
        self.dfs(r+1, c, rooms, d+1)
        self.dfs(r-1, c, rooms, d+1)
        self.dfs(r, c+1, rooms, d+1)
        self.dfs(r, c-1, rooms, d+1)


rooms = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647]]

Solution().wallsAndGates(rooms)
print(rooms)
