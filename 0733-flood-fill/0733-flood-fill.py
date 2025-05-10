class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row_len = len(image)
        col_len = len(image[0])
        visited = [[0] * col_len for _ in range(row_len)]
        initial_col = image[sr][sc]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(row, col):
            nonlocal visited
            queue = deque()
            queue.append((row, col))
            
            while queue:
                r, c = queue.popleft()
                image[r][c] = color
                visited[r][c] = 1

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < row_len and 0 <= nc < col_len and image[nr][nc] == initial_col and visited[nr][nc] != 1:
                        queue.append((nr, nc))



        def dfs(row, col):
            nonlocal visited
            image[row][col] = color
            visited[row][col] = 1

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if (0 <= nr < row_len and 0 <= nc < col_len and image[nr][nc] == initial_col and visited[nr][nc] != 1):
                    dfs(nr, nc)

        bfs(sr, sc)
        return image
