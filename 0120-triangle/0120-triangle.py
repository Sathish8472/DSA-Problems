class Solution:
     
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0] * n for _ in range(n)]

        for j in range(n):
            dp[n - 1][j] = triangle[n - 1][j]
        
        print(dp)

        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dn = triangle[i][j] + dp[i + 1][j]
                dg = triangle[i][j] + dp[i + 1][j + 1]

                dp[i][j] = min(dn, dg)
        
        return dp[0][0]



    # Dp - Memoization
    # Time: O(N)
    # Space: O(N) + O(N) stack space
    def minimumTotal_2(self, triangle: List[List[int]]) -> int:

        m = len(triangle)
        n = len(triangle)

        if n == 1 and m == 1:
            return triangle[0][0]

        dp = [[-1] * n for _ in range(m)]
        self._solve(triangle, 0, 0, dp)

        return dp[0][0]

    def _solve(self, triangle, i, j, dp):
        n = len(triangle)

        if i == n - 1:
            return triangle[i][j]
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        dn = triangle[i][j] + self._solve(triangle, i + 1, j, dp)

        dg = triangle[i][j] + self._solve(triangle, i + 1, j + 1, dp)

        dp[i][j] = min(dn, dg)

        return dp[i][j]


    # Recursion
    # time: 2 ^ N
    # Space: O(N)
    def minimumTotal_1(self, triangle: List[List[int]]) -> int:

        return self._solve1(triangle, 0, 0)

    def _solve1(self, triangle, i, j):
        n = len(triangle)

        if i == n - 1:
            return triangle[i][j]
        
        dn = triangle[i][j] + self._solve(triangle, i + 1, j)

        dg = triangle[i][j] + self._solve(triangle, i + 1, j + 1)

        return min(dn, dg)