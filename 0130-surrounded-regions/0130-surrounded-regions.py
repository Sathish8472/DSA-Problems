class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])

        visited = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and  board[i][j] == "O" and visited[i][j] != 1:
                    self.dfs(i, j, board, visited, m, n)


        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and visited[i][j] == 0:
                    board[i][j] = "X"
        

    def dfs(self, row, col, board, visited, m, n):
        stack = []

        visited[row][col] = 1
        stack.append((row, col))

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while stack:
            r, c = stack.pop()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == "O" and visited[nr][nc] != 1:
                    stack.append((nr, nc))
                    visited[nr][nc] = 1
        