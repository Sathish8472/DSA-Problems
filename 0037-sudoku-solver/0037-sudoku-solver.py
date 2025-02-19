class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + (c // 3)].add(num)

        def is_valid(board, row, col, num):
            return (
                num not in rows[row]
                and num not in cols[col]
                and num not in boxes[(row // 3) * 3 + (col // 3)]
            )

        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for num in map(str, range(1, 10)):
                            if is_valid(board, r, c, num):
                                board[r][c] = num
                                rows[r].add(num)
                                cols[c].add(num)
                                boxes[(r // 3) * 3 + (c // 3)].add(num)

                                if backtrack():
                                    return True
                                board[r][c] = "."
                                if num in rows[r]:
                                    rows[r].remove(num)
                                if num in cols[c]:
                                    cols[c].remove(num)
                                if num in boxes[(r // 3) * 3 + (c // 3)]:
                                   boxes[(r // 3) * 3 + (c // 3)].remove(num)

                        return False
            return True

        backtrack()

    def solveSudoku_1(self, board: List[List[str]]) -> None:

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
