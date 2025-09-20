class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        prev = [0] * n

        for i in range(m):
            temp = [0] * n

            for j in range(n):
                if i >= 0 and j >= 0 and obstacleGrid[i][j] == 1:
                    temp[j] = 0
                elif i == 0 and j == 0:
                    temp[j] = 1
                else:
                    temp[j] = temp[j - 1] + prev[j]
            prev = temp

        return prev[-1]

    


    def uniquePathsWithObstacles_2(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[-1] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i >= 0 and j >= 0 and obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    right = dp[i][j - 1] if j > 0 else 0
                    bottom = dp[i - 1][j] if i > 0 else 0

                    dp[i][j] = right + bottom
        
        return dp[m - 1][n - 1]

    
    
    
    
    def uniquePathsWithObstacles_1(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[-1] * n for _ in range(m)]

        return self._solve(obstacleGrid, m - 1, n - 1, dp)

    
    def _solve(self, obstacleGrid, i, j, dp):

        if i >= 0 and j >= 0 and obstacleGrid[i][j] == 1:
            return 0
        elif i == 0 and j == 0:
            return 1
        elif i < 0 or j < 0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        left = 0
        if j > 0:
            left = self._solve(obstacleGrid, i, j - 1, dp)
        up = 0
        
        if i > 0:
            up = self._solve(obstacleGrid, i - 1, j, dp)

        dp[i][j] = left + up

        return dp[i][j]

        
        