'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

E = unrevealed empty
B = revealed, empty, no adj mines
dig1~8 = revealed, empty, 1~8 adj mines

M = unrevealed mine
X = revealed mine
'''

from pprint import pprint


class Solution(object):
    def updateBoard(self, board, click):
        '''
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        '''
        if not board:
            return []

        ROL, COL = len(board), len(board[0])
        i, j = click[0], click[1]

        # If a mine ('M') is revealed, then the game is over - change it to 'X'.
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board

        # 8 directions
        DIR = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]

        def dfs(i, j):
            if board[i][j] != 'E':
                return

            mine_count = 0

            for d in DIR:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < ROL and 0 <= nj < COL and board[ni][nj] == 'M':        
                    mine_count += 1

            if mine_count == 0:
                board[i][j] = 'B'
            else:
                board[i][j] = str(mine_count)
                return

            for d in DIR:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < ROL and 0 <= nj < COL:
                    dfs(ni, nj)

        # run dfs to reveal the board
        dfs(i, j)
        return board


b = [
        ['E','E','E','E','E'],
        ['E','E','M','E','E'],
        ['E','E','E','E','E'],
        ['E','E','E','E','E']
]
c = [3,0]
pprint(Solution().updateBoard(b, c))
