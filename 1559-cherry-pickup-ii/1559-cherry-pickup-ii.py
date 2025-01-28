# Recursion: , Time: O(9 ^ n) × O(m ^ 2), Sp: O(N)
class Solution:

    def func(self, i, j1, j2, n, m, grid, dp):
        if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
            return -int(1e9)

        if i == n - 1:
            if j1 == j2:
                return grid[i][j1]
            else:
                return grid[i][j1] + grid[i][j2]

        # If result already computed
        if dp[i][j1][j2] != -1:
            return dp[i][j1][j2]

        # Try all possible moves for both positions j1, j2
        maxi = -int(1e9)

        for di in range(-1, 2):
            for dj in range(-1, 2):
                if j1 == j2:
                    ans = grid[i][j1] + self.func(i + 1, j1 + di, j2 + dj, n, m, grid, dp)
                else:
                    ans = (
                        grid[i][j1]
                        + grid[i][j2]
                        + self.func(i + 1, j1 + di, j2 + dj, n, m, grid, dp)
                    )

                maxi = max(maxi, ans)

        dp[i][j1][j2] = maxi
        return maxi

    def cherryPickup(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        # Initialize memoization table with -1
        dp = [[[-1 for j in range(m)] for i in range(m)] for k in range(n)]

        return self.func(0, 0, m - 1, n, m, grid, dp)


# Recursion: , Time: O(9 ^ n) × O(m ^ 2), Sp: O(N)
class Solution1:

    def func(self, i, j1, j2, n, m, grid):
        if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
            return -1e9

        if i == n - 1:
            if j1 == j2:
                return grid[i][j1]
            else:
                return grid[i][j1] + grid[i][j2]

        # Try all possible moves for both positions j1, j2
        maxi = -float("inf")
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if j1 == j2:
                    ans = grid[i][j1] + self.func(i + 1, j1 + di, j2 + dj, n, m, grid)
                else:
                    ans = (
                        grid[i][j1]
                        + grid[i][j2]
                        + self.func(i + 1, j1 + di, j2 + dj, n, m, grid)
                    )

                maxi = max(maxi, ans)

        return maxi

    def cherryPickup(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        return self.func(0, 0, m - 1, n, m, grid)
