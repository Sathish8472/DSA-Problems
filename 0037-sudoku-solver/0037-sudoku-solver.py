class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        def isValid(board, row, col, num):
            for i in range(9):
                if board[row][i] == num:
                    return False
                if board[i][col] == num:
                    return False
                if board[3 * (row // 3) + (i // 3)][3 * (col // 3) + (i % 3)] == num:
                    return False
            return True

        def backtrack():

            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for num in map(str, range(1, 10)):
                            if isValid(board, i, j, num):
                                board[i][j] = num

                                if backtrack():
                                    return True
                                board[i][j] = "."
                        return False

            return True

        backtrack()
