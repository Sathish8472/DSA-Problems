class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        prev = matrix[0][:]

        for i in range(1, n):
            curr = [0] * m

            for j in range(m):
                up = prev[j]
                left_dg = prev[j - 1] if j - 1 >= 0 else float('inf')
                right_dg = prev[j + 1] if j + 1 < m else float('inf')
                curr[j] = matrix[i][j] + min(up, left_dg, right_dg)
            
            prev = curr
        
        return min(prev)




    def minFallingPathSum1(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        dp = [[0] * m for _ in range(n)]

        for j in range(m):
            dp[0][j] = matrix[0][j]
        
        for i in range(1, n):
            for j in range(m):
                
                up = dp[i-1][j]
                left_diag = dp[i-1][j-1] if j-1 >= 0 else float('inf')
                right_diag = dp[i-1][j+1] if j+1 < m else float('inf')

                dp[i][j] = matrix[i][j] + min(up, left_diag, right_diag)

        return min(dp[-1])
    

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