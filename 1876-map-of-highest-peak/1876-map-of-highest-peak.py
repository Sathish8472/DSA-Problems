class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        row_len = len(isWater)
        col_len = len(isWater[0])

        visited = [[0] * col_len for _ in range(row_len)]
        dist = [[0] * col_len for _ in range(row_len)]

        queue = deque()

        for r in range(row_len):
            for c in range(col_len):
                if isWater[r][c] == 1:
                    queue.append((r, c, 0))
                    visited[r][c] = 1
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            r, c, steps = queue.popleft()
            dist[r][c] = steps

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < row_len and 0 <= nc < col_len and visited[nr][nc] != 1:
                    queue.append((nr, nc, steps + 1))
                    visited[nr][nc] = 1

        return dist