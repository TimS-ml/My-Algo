'''
lc 529 extend

E = unrevealed empty
B = revealed, empty, no adj mines
dig1~8 = revealed, empty, 1~8 adj mines

* = unrevealed mine
x = revealed mine
'''

from pprint import pprint
import random

random.seed(0)

class mineSweeper:
    def __init__(self, board):
        self.row = len(board)
        self.col = len(board[0])
        self.board = board

        # 8 directions
        self.DIR = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]

    @classmethod
    def genBoard(cls, row=9, col=10, numMine=10):
        # method 1
        # boardCoord = [(x, y) for x in range(row) for y in range(col)]
        # mineCoord = random.choices(boardCoord, k=numMine)

        # method 2
        boardCoord = [(x, y) for x in range(row) for y in range(col)]
        mineCoord = random.sample(boardCoord, k=numMine)

        board = [['E' for _ in range(col)] for _ in range(row)]
        
        for x, y in mineCoord:
            board[x][y] = '*'
        # pprint(self.mineCoord)
        return cls(board)

    @classmethod
    def assignBoard(cls, board):
        return cls(board)

    def click(self, x, y):
        pprint(self.board)
        if self.board[x][y] == '*':
            self.board[x][y] = 'x'
            print('Dead')
            print(self.board)
            return

        def dfs(x, y):
            # if visited
            if self.board[x][y] != 'E':
                return 

            mineCount = 0
            
            for movX, movY in self.DIR:
                newX, newY = x + movX, y + movY
    
                if 0 <= newX < self.row and 0 <= newY < self.col and self.board[newX][newY] == '*':
                    mineCount += 1
    
            if mineCount > 0:
                self.board[x][y] = str(mineCount)
                # we should stop there
                return
            else:
                self.board[x][y] = 'B'

            for movX, movY in self.DIR:
                newX, newY = x + movX, y + movY
    
                if 0 <= newX < self.row and 0 <= newY < self.col and self.board[newX][newY] == 'E':
                    dfs(newX, newY)

        dfs(x, y)
        pprint(self.board)
        return


b = [
        ['E','E','E','E','E'],
        ['E','E','*','E','E'],
        ['E','E','E','E','E'],
        ['E','E','E','E','E']
]

# M = mineSweeper.genBoard()
M = mineSweeper(b)
M.click(3, 0)
