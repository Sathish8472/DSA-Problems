class Solution:
    
    # Space Optimation
    # Time: O(M * N)
    # SpacE: O(N)
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [0] * n

        for i in range(m):
            temp = [0] * n
            for j in range(n):
                if i == 0 and j == 0:
                    temp[j] = 1
                    continue

                up = prev[j] if i > 0 else 0
                left = temp[j - 1] if j > 0 else 0

                temp[j] = up + left
            
            prev = temp
        
        return prev[-1]


    # DP - tabulation - Bottom up
    # Time: O(M * N)
    # Space: O(M * N)
    def uniquePaths_3(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    bottom = 0
                    right = 0
                    if i > 0:
                        bottom = dp[i - 1][j]
                    if j > 0:
                        right = dp[i][j - 1]

                    dp[i][j] = bottom + right

        return dp[m - 1][n - 1]

    

    # DP - Memoization - Top Down
    # time: O(M * N)
    # Space: O(M + N) + O(M * N)
    def uniquePaths_2(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]

        def _solve(i, j, dp):
            if i == 0 and j == 0:
                return 1
            
            if i < 0 or j < 0:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
                
            left = _solve(i, j - 1, dp)
            up = _solve(i - 1, j, dp)

            dp[i][j] = left + up
            print(f"i: {i}, j: {j}, dp[{i}][{j}] = {dp[i][j]}", )
            return dp[i][j]
        
        return _solve(m - 1, n - 1, dp)


    # Brute - Recursion
    # Time: 2 ^ (m * n)
    # Space: O(m + n)
    def uniquePaths_1(self, m: int, n: int) -> int:
    
        def _solve(i, j):
            if i == 0 and j == 0:
                return 1
            
            if i < 0 or j < 0:
                return 0
                
            left = _solve(i, j - 1)
            up = _solve(i - 1, j)

            return left + up
        
        return _solve(m - 1, n - 1)