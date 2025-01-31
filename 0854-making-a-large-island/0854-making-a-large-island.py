class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        n = len(grid)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        island_id = 2
        island_size = {}

        def dfs(i, j, island_id):
            """DFS to mark the island and calculate size"""
            if i < 0 or j < 0 or i >= n or j >= n or grid[i][j] != 1:
                return 0
            grid[i][j] = island_id
            size = 1
            for dx, dy in dirs:
                size += dfs(i + dx, j + dy, island_id)
            return size

        def bfs(i, j, island_id):
            """BFS to mark the island and calculate size"""
            queue = deque([(i, j)])
            grid[i][j] = island_id
            size = 1
            while queue:
                x, y = queue.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = island_id
                        queue.append((nx, ny))
                        size += 1
            return size

        # Step 1: Identify islands and store their sizes
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    size = dfs(i, j, island_id)
                    island_size[island_id] = size
                    island_id += 1

        max_island = max(island_size.values(), default=0)

        # Step 2: Check flipping each `0`
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    new_size = 1
                    for dx, dy in dirs:
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < n and grid[x][y] > 1:
                            island_id = grid[x][y]
                            if island_id not in seen:
                                new_size += island_size[island_id]
                                seen.add(island_id)
                    max_island = max(max_island, new_size)

        return max_island
