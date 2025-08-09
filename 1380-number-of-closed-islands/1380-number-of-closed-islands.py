class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        
        visited = [[0] * col_len for _ in range(row_len)]
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for r in range(row_len):
            for c in range(col_len):
                if (r == 0 or r == row_len - 1 or c == 0 or c == col_len - 1) and grid[r][c] == 0 and visited[r][c] != 1:
                    # self.dfs(r, c, visited, grid, row_len, col_len)
                    self.bfs(r, c, visited, grid, row_len, col_len)

        closed_islands = 0
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == 0 and visited[r][c] != 1:
                    # self.dfs(r, c, visited, grid, row_len, col_len)
                    self.bfs(r, c, visited, grid, row_len, col_len)
                    closed_islands += 1
        
        return closed_islands

    def dfs(self, row, col, visited, grid, row_len, col_len):
            visited[row][col] = 1

            for dx, dy in self.directions:
                nr = row + dx
                nc = col + dy

                if 0 <= nr < row_len and 0 <= nc < col_len and grid[nr][nc] == 0 and visited[nr][nc] != 1:
                    self.dfs(nr, nc, visited, grid, row_len, col_len)

    def bfs(self, row, col, visited, grid, row_len, col_len):
        queue = deque()
        queue.append((row, col))
        visited[row][col] = 1

        while queue:
            r, c = queue.popleft()

            for dx, dy in self.directions:
                nr = r + dx
                nc = c + dy

                if 0 <= nr < row_len and 0 <= nc < col_len and grid[nr][nc] == 0 and visited[nr][nc] != 1:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))
