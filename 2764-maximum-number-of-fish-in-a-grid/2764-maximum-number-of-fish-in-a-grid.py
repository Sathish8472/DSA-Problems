class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False] * n for _ in range(m)]

        def isValid(x, y):
            return (
                0 <= x < m
                and 0 <= y < n
                and grid[x][y] > 0
                and not visited[x][y]
            )

        def dfs(x, y):
            visited[x][y] = True
            fish = grid[x][y]

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if isValid(nx, ny):
                    fish += dfs(nx, ny)

            return fish

        maxFish = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                    maxFish = max(maxFish, dfs(i, j))

        return maxFish
