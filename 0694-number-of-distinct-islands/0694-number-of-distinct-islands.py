class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        
        visited = [[0] * col_len for _ in range(row_len)]
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        distinct_islands = set()
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == 1 and visited[r][c] != 1:
                    path = []
                    # self.dfs(r, c, r, c, grid, visited, path, row_len, col_len)
                    self.bfs(r, c, r, c, grid, visited, path, row_len, col_len)
                    distinct_islands.add(tuple(path))

        return len(distinct_islands)

    def dfs(self, row, col, base_row, base_col, grid, visited, path, row_len, col_len):
            path.append((row - base_row, col - base_col))
            visited[row][col] = 1

            for dx, dy in self.directions:
                nr = row + dx
                nc = col + dy

                if 0 <= nr < row_len and 0 <= nc < col_len and grid[nr][nc] == 1 and visited[nr][nc] != 1:
                    self.dfs(nr, nc, base_row, base_col, grid, visited, path, row_len, col_len)
    
    def bfs(self, row, col, base_row, base_col, grid, visited, path, row_len, col_len):
        queue = deque()
        queue.append((row, col))
        visited[row][col] = 1

        while queue:
            r, c = queue.popleft()
            path.append((r - base_row, c - base_col))

            for dx, dy in self.directions:
                nr = r + dx
                nc = c + dy
                if 0 <= nr < row_len and 0 <= nc < col_len and grid[nr][nc] == 1 and visited[nr][nc] != 1:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))

