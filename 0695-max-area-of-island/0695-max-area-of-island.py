class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        visited = [[0 for _ in range(n)] for _ in range(m)]
        max_islands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] != 1:
                    islands = self.dfs(i, j, grid, visited, m, n)
                    max_islands = max(max_islands, islands)
        
        return max_islands
    
    def dfs(self, row, col, grid, visited, m, n):
        visited[row][col] = 1
        islands = 1
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for dx, dy in directions:
            nr = row + dx
            nc = col + dy

            if 0 <= nr < m and 0 <= nc < n and visited[nr][nc] != 1 and grid[nr][nc] == 1:
                islands += self.dfs(nr, nc, grid, visited, m, n)

        return islands