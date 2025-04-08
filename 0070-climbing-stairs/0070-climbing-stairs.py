class Solution:

    # DP - Iterative - Tabulation - bottom up
    # Time: O(N), Space; O(1)
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        
        prev2 = 1
        prev = 1

        for i in range(2, n + 1):
            curi = prev2 + prev
            prev2 = prev
            prev = curi
        
        return prev

    


    # Dp - Iterative - Bottom up - Tabulation
    # Time: O(N), Space: O(N) 
    def climbStairs_2(self, n: int) -> int:
        dp = [-1] * (n + 1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]




    
    # DP - Topdown - Memoization - Recusion
    # The function _helper(n) is called recursively, but with memoization, each value of n n is computed only once.
    # Time: O(N), Space: O(N)
    def climbStairs_1(self, n: int) -> int:
        dp = [-1] * (n + 1)         # Memoization

        def _helper(n):
            nonlocal dp
            if n <= 1:
                dp[n] = 1
                return 1

            if dp[n] != -1:
                return dp[n]

            dp[n] = _helper(n - 1) + _helper(n - 2) 
            return dp[n]

        _helper(n)
        return dp[n]
    

    # Recursion
    # Time: 2 ^ n, Space: O(N)
    def climbStairs_1(self, n: int) -> int:
        if n <= 1:
            return 1                # This is very important

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)