class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        row_len, col_len = len(heights), len(heights[0])

        pacific = [[False] * col_len for _ in range(row_len)] 
        atlantic = [[False] * col_len for _ in range(row_len)] 

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(row, col, reachable):
            if reachable[row][col]:
                return
            
            reachable[row][col] = True

            for dx, dy in directions:
                nr = row + dx
                nc = col + dy
                if 0 <= nr < row_len and 0 <= nc < col_len and heights[nr][nc] >= heights[row][col]:
                    dfs(nr, nc, reachable)
            

        # pacific area
        for r in range(row_len):
            dfs(r, 0, pacific)
        
        for c in range(col_len):
            dfs(0, c, pacific)
        
        # Atlantic
        for r in range(row_len):
            dfs(r, col_len - 1, atlantic)

        for c in range(col_len):
            dfs(row_len - 1, c, atlantic)
        
        result = []
        for r in range(row_len):
            for c in range(col_len):
                if pacific[r][c] and atlantic[r][c]:
                    result.append([r, c])
        
        return result

        