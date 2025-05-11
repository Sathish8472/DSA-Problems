class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        visited = [[0] * col_len for _ in range(row_len)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        distinct_islands = set()

        def dfs(row, col, base_row, base_col, path):
            path.append((row - base_row, col - base_col))
            visited[row][col] = 1

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < row_len and 0 <= nc < col_len and grid[nr][nc] == 1 and visited[nr][nc] != 1:
                    dfs(nr, nc, base_row, base_col, path)

        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == 1 and visited[r][c] != 1:
                    path = []
                    visited[r][c] = 1
                    dfs(r, c, r, c, path)
                    distinct_islands.add(tuple(path))

        return len(distinct_islands)