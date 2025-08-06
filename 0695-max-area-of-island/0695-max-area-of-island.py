class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])

        visited = [[0] * col_len for _ in range(row_len)]

        island_max_area = 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(row, col):
            visited[row][col] = 1
            area = 1

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < row_len and 0 <= nc < col_len and grid[nr][nc] == 1 and visited[nr][nc] != 1:
                    area += dfs(nr, nc)

            return area

        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == 1 and visited[r][c] != 1:
                    area = dfs(r, c)
                    island_max_area = max(island_max_area, area)

        return island_max_area