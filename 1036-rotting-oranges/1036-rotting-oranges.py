class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        
        rotten_oranges = deque()
        fresh_oranges = 0

        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == 2:
                    rotten_oranges.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        print("fresh_oranges: ", fresh_oranges)

        if fresh_oranges == 0:
            return 0
        
        minutes = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while rotten_oranges:
            minutes += 1

            for _ in range(len(rotten_oranges)):
                r, c = rotten_oranges.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < row_len and 0 <= nc < col_len and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_oranges -= 1
                        rotten_oranges.append((nr, nc))
            
            if fresh_oranges == 0:
                return minutes

        return -1