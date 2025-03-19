class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        count = 0

        visited = [[0] * col_len for _ in range(row_len)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


        def dfs(row, col):
            visited[row][col] = 1

            for dr, dc in directions:
                nrow, ncol = row + dr, col + dc
                if 0 <= nrow < row_len and 0 <= ncol < col_len and grid[nrow][ncol] == "1" and not visited[nrow][ncol]:
                    dfs(nrow, ncol)



        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            visited[row][col] = 1
            
            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nrow, ncol = r + dr, c + dc
                    if 0 <= nrow < row_len and 0 <= ncol < col_len and grid[nrow][ncol] == "1" and not visited[nrow][ncol]:
                        visited[nrow][ncol] = 1
                        queue.append((nrow, ncol))


        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == "1" and not visited[i][j]:
                    count += 1
                    dfs(i, j)

            
        
        return count

        