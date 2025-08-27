class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        DIRS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]  # ↘ ↙ ↖ ↗
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(x, y, direction, can_turn, target):
            dx, dy = DIRS[direction]
            nx, ny = x + dx, y + dy

            # Out of bounds or value mismatch
            if not (0 <= nx < m and 0 <= ny < n) or grid[nx][ny] != target:
                return 0

            next_target = 2 if target == 0 else 0  # alternate between 2 and 0

            # Continue in same direction
            max_len = dfs(nx, ny, direction, can_turn, next_target)

            # Try one clockwise turn if allowed
            if can_turn:
                new_dir = (direction + 1) % 4
                max_len = max(max_len, dfs(nx, ny, new_dir, False, next_target))

            return max_len + 1

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for direction in range(4):
                        result = max(result, dfs(i, j, direction, True, 2) + 1)

        return result

 


    def lenOfVDiagonal1(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

        turn_map = {
            (1, 1): (1, -1),
            (1, -1): (-1, -1),
            (-1, -1): (-1, 1),
            (-1, 1): (1, 1),
        }

        def in_bounds(x, y):
            return 0 <= x < n and 0 <= y < m

        def expected_value(step):
            if step == 0:
                return 1
            return 2 if step % 2 == 1 else 0

        def dfs(x, y, dx, dy, step, turned):
            if not in_bounds(x, y) or grid[x][y] != expected_value(step):
                return step

            length = dfs(x + dx, y + dy, dx, dy, step + 1, turned)

            if not turned:
                new_dx, new_dy = turn_map[(dx, dy)]
                length = max(
                    length, dfs(x + new_dx, y + new_dy, new_dx, new_dy, step + 1, True)
                )

            return length

        max_len = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for dx, dy in directions:
                        mlength = dfs(i, j, dx, dy, 0, False)
                        max_len = max(max_len, mlength)

        return max_len
