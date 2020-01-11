# https://leetcode-cn.com/problems/surrounded-regions/


class Solution(object):
    def solve(self, board):
        if not board or not board[0]:
            return
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                # border case
                if (i == 0 or j == 0 or i == m-1 or j == n-1) and board[i][j] == 'O':
                    board[i][j] == 'M'
                    self.dfs(i, j, board)
        # print(board)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'M':
                    board[i][j] = 'O'
        print(board)

    def dfs(self, r, c, board):
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] == 'X' or board[r][c] == 'M':
            return
        # region that connect to border case and not border
        board[r][c] = 'M'
        self.dfs(r+1, c, board)
        self.dfs(r-1, c, board)
        self.dfs(r, c+1, board)
        self.dfs(r, c-1, board)


board1 = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]]
board2 = [
    ["X", "X", "X", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "O", "X"],
    ["X", "O", "X", "X"]]
Solution().solve(board2)
