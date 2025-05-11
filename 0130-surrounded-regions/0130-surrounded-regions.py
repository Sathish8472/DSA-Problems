class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row_len = len(board)
        col_len = len(board[0])

        visited = [[0] * col_len for _ in range(row_len)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(row, col):
            print(f"dfs: {row}, {col}")
            visited[row][col] = 1

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if 0 <= nr < row_len and 0 <= nc < col_len and board[nr][nc] == 'O' and visited[nr][nc] != 1:
                    dfs(nr, nc)

        for i in range(row_len):
            for j in range(col_len):
                if (i == 0 or i == row_len - 1 or j == 0 or j == col_len - 1) and board[i][j] == 'O' and visited[i][j] != 1:
                    dfs(i, j)

        print("Vis: ", visited)

        for i in range(row_len):
            for j in range(col_len):
                if board[i][j] == 'O' and visited[i][j] != 1:
                    board[i][j] = 'X'
                


        