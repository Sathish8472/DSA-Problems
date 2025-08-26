class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = ["." * n for _ in range(n)]

        self.place_queens(0, ans, board)
        return ans

    def place_queens(self, col, ans, board):
        if col == len(board):
            ans.append(list(board))
            return
        
        for row in range(len(board)):
            if self.safe(board, row, col):
                board[row] = board[row][:col] + "Q" + board[row][col + 1:]
                self.place_queens(col + 1, ans, board)
                board[row] = board[row][:col] + "." + board[row][col+1:]
    
    def safe(self, board, row, col):
        r, c = row, col

        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1

        r, c = row, col
        while c >= 0:
            if board[r][c] == "Q":
                return False
            c -= 1

        r, c = row, col
        while r < len(board) and c >= 0:
            if board[r][c] == "Q":
                return False
            r += 1
            c -= 1

        return True 

        