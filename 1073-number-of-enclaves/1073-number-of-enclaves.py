class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])

        visited = [[0] * col_len for _ in range(row_len)]

        for i in range(row_len):
            for j in range(col_len):
                if (i == 0 or j == 0 or i == row_len - 1 or j == col_len - 1) and grid[i][j] == 1:
                    visited[i][j] = 1
                    self.bfs(i, j, grid, visited, row_len, col_len) 
                    
        count = 0

        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == 1 and visited[i][j] != 1:
                    count += 1

        return count

    
    def bfs(self, row, col, grid, visited, row_len, col_len):
            queue = deque()
            queue.append((row, col))

            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < row_len and 0 <= nc < col_len and grid[nr][nc] == 1 and visited[nr][nc] != 1:
                        visited[nr][nc] = 1
                        queue.append((nr, nc))