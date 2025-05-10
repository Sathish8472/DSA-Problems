class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        total_islands = 0

        visited = [[0] * n for _ in range(m)]
        print(visited)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    self.bfs(grid, i, j, visited, m, n)
                    total_islands += 1

        return total_islands


    def dfs(self, grid, row, col, visited, m, n):
        visited[row][col] = 1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            nr = row + dr
            nc = col + dc

            if nr >= 0 and nr < m and nc >= 0 and nc < n and grid[nr][nc] == '1' and visited[nr][nc] != 1:
                self.dfs(grid, nr, nc, visited, m, n)

    
    def bfs(self, grid, row, col, visited, row_len, col_len):
            queue = deque()
            queue.append((row, col))
            visited[row][col] = 1
            
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nrow, ncol = r + dr, c + dc
                    if 0 <= nrow < row_len and 0 <= ncol < col_len and grid[nrow][ncol] == "1" and not visited[nrow][ncol]:
                        visited[nrow][ncol] = 1
                        queue.append((nrow, ncol))


