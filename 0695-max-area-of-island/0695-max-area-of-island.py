class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])

        visited = [[0] * col_len for _ in range(row_len)]

        island_max_area = 0

        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == 1 and visited[r][c] != 1:
                    # area = self.dfs(r, c, visited, grid, row_len, col_len)
                    area = self.bfs(r, c, visited, grid, row_len, col_len)
                    island_max_area = max(island_max_area, area)

        return island_max_area

    def dfs(self, row, col, visited, grid, row_len, col_len):
        visited[row][col] = 1
        area = 1

        for dr, dc in self.directions:
            nr = row + dr
            nc = col + dc
            if 0 <= nr < row_len and 0 <= nc < col_len and grid[nr][nc] == 1 and visited[nr][nc] != 1:
                area += self.dfs(nr, nc, visited, grid, row_len, col_len)

        return area

    def bfs(self, row, col, visited, grid, row_len, col_len):
        queue = deque()
        queue.append((row, col))
        visited[row][col] = 1
        area = 1

        while queue:
            r, c = queue.popleft()

            for dx, dy in self.directions:
                nr = r + dx
                nc = c + dy
                if 0 <= nr < row_len and 0 <= nc < col_len and grid[nr][nc] == 1 and visited[nr][nc] != 1:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))
                    area += 1

        return area
