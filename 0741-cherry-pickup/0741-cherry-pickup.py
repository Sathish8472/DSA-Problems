class Solution:

    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[-1] * n for _ in range(n)] for _ in range(n)]

        return max(0, self.func(0, 0, 0, n, grid, dp))
    
    def func(self, r1, c1, c2, n, grid, dp):
        r2 = r1 + c1 - c2
        if r1 >= n or c1 >= n or r2 >= n or c2 >= n:
            return -10**9
        
        if grid[r1][c1] == -1 or grid[r2][c2] == -1:
            return -10**9
        
        if r1 == n - 1 and c1 == n - 1:
            return grid[r1][c1]
        
        if dp[r1][c1][c2] != -1:
            return dp[r1][c1][c2]
        
        cherries = grid[r1][c1]
        if (r1, c1) != (r2, c2):
            cherries += grid[r2][c2]
        
        best_next = max(
            self.func(r1 + 1, c1, c2, n, grid, dp),
            self.func(r1, c1 + 1, c2, n, grid, dp),
            self.func(r1 + 1, c1, c2 + 1, n, grid, dp),
            self.func(r1, c1 + 1, c2 + 1, n, grid, dp))

        dp[r1][c1][c2] = cherries + best_next
        return dp[r1][c1][c2]


    # Brute
    def cherryPickup1(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def dfs(r, c, collected):
            if r < 0 or c < 0 or r >= n or grid[r][c] == -1:
                return float('-inf')
            
            cherries = grid[r][c]
            grid[r][c] = 0

            if r == n - 1 and c == n - 1:
                res = returnTrip(grid, n)
            else:
                res = max(dfs(r + 1, c, collected), dfs(r, c + 1, collected))

            grid[r][c] = cherries
            return cherries + res
        
        def returnTrip(grid, n):
            def dfs2(r, c):
                if r < 0 or c < 0 or r >= n or c >= n or grid[r][c] == -1:
                    return float('-inf')
                
                cherries = grid[r][c]
                grid[r][c] = 0

                if r == 0 and c == 0:
                    res = 0
                else:
                    res = max(dfs2(r - 1, c), dfs2(r, c - 1))
                
                grid[r][c] = cherries
                return cherries + res
            
            return dfs2(n - 1, n - 1)

        ans = dfs(0, 0, 0)
        return max(0, ans)