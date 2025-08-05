class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        fresh_oranges = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    queue.append((i, j, 0))

        if fresh_oranges == 0:
            return 0

        time = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            row, col, t = queue.popleft()
            time = max(time, t)

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_oranges -= 1
                    queue.append((nr, nc, t + 1))

        if fresh_oranges != 0:
            return -1

        return time

        