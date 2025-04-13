class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        dp = [[0 for j in range(m)] for i in range(n)]

        for j in range(m):
            dp[0][j] = matrix[0][j]
        
        for i in range(1, n):
            for j in range(m):

                up = matrix[i][j] + dp[i - 1][j]

                left_dg = matrix[i][j]
                if j - 1 >= 0:
                    left_dg += dp[i - 1][j - 1]
                else:
                    left_dg += float('inf')
                
                right_dg = matrix[i][j]
                if j + 1 < m:
                    right_dg += dp[i - 1][j + 1]
                else:
                    right_dg += float('inf')

                dp[i][j] = min(up, left_dg, right_dg)

            
        min_sum = float('inf')

        for j in range(m):
            min_sum = min(min_sum, dp[n - 1][j])

        return min_sum
    

    def minFallingPathSum_2(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[-1] * n for _ in range(n)]

        min_sum = float('inf')
        for j in range(n):
            cur_min = self._find_min_falling_path_sum(matrix, 0, j, n, dp)
            min_sum = min(min_sum, cur_min)
        
        return min_sum

    
    def _find_min_falling_path_sum(self, matrix, i, j, n, dp):
        if i < 0 or j < 0 or i >= n or j >= n:
            return float('inf')
        
        if i == n - 1:
            return matrix[i][j]
        
        left_dg = matrix[i][j] + self._find_min_falling_path_sum(matrix, i + 1, j - 1, n, dp)
        down = matrix[i][j] + self._find_min_falling_path_sum(matrix, i + 1, j, n, dp)
        right_dg = matrix[i][j] + self._find_min_falling_path_sum(matrix, i + 1, j + 1, n, dp)

        dp[i][j] = min(down, min(left_dg, right_dg))

        return dp[i][j]

    

    def minFallingPathSum_1(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        max_i = float('inf')

        for j in range(n):
            curi = self._solve(matrix, 0, j, n)
            max_i = min(max_i, curi)

        return max_i

    def _solve(self, matrix, i, j, n):
        if i < 0 or j < 0 or i >= n or j >= n:
            return float('inf')

        if i == n - 1:
            return matrix[i][j]
        
        left_dg = matrix[i][j] + self._solve(matrix, i + 1, j - 1, n)
        down = matrix[i][j] + self._solve(matrix, i + 1, j, n)
        right_dg = matrix[i][j] + self._solve(matrix, i + 1, j + 1, n)

        return min(down, min(left_dg, right_dg))