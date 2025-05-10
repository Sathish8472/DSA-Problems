class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row_len = len(image)
        col_len = len(image[0])
        initial_col = image[sr][sc]

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        result = [row[:] for row in image]

        def bfs(row, col):
            if result[row][col] == color: 
                return

            queue = deque()
            queue.append((row, col))
            
            while queue:
                r, c = queue.popleft()
                image[r][c] = color

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < row_len and 0 <= nc < col_len and result[nr][nc] == initial_col:
                        result[nr][nc] = color
                        queue.append((nr, nc))

        def dfs(row, col):
            if result[row][col] == color: 
                return

            result[row][col] = color

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if 0 <= nr < row_len and 0 <= nc < col_len and result[nr][nc] == initial_col:
                    dfs(nr, nc)

        bfs(sr, sc)
        return result
