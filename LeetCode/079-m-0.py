from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # wrong dir
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def search(i, j, wi):
            if len(word) == wi:
                return True
            if i >= len(board) or j >= len(board[0]) \
                or i < 0 or j < 0:
                return False
            
            # print(i, j, wi, board[i][j], word[wi])
            if board[i][j] != word[wi]:
                return False

            for d in dir:
                newR, newC = i + d[0], j + d[1]
                if search(newR, newC, wi + 1):
                    return True

            return False
        
        # find start point
        for r in range(len(board)):
            for c in range(len(board)):
                if w[0] == board[r][c]:
                    print(board[r][c])
                    if search(r, c, 0):
                        return True

        return False


b = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
w = "ABCCED"
print(Solution().exist(b, w))
