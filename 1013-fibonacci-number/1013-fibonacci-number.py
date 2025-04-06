class Solution:

    # DP - Iterative - Bottom up
    # time: O(N)
    # Space: Constant
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        prev2, prev = 0, 1

        for _ in range(2, n + 1):
            curi = prev + prev2
            prev2 = prev
            prev = curi

        return prev

    

    # DP - Iterative - bottom Up - Tabulation
    # Time: O(N), 
    # Space: O(N) -> For Extra space
    def fib_3(self, n: int) -> int:

        if n <= 1:
            return n
        
        dp = [0] * (n + 1)      
        dp[0] = 0               # Bottom Up, solve base problem first
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]





    # DP - Memoization - Top down
    # Time: O(N), 
    # Space: O(N) -> For Extra space + Recursion depth
    def fib_2(self, n: int) -> int:
        
        dp = [-1] * (n + 1)             # Called: memoization

        def _helper(n, dp):
            if n <= 1:
                dp[n] = n
                return n

            if dp[n] != -1:
                return dp[n]
            
            dp[n] = _helper(n - 1, dp) + _helper(n - 2, dp) 
            print(dp)
            return dp[n]

        result = _helper(n, dp)
        print(dp)
       
        return result



    # Recursion : Calls itself again and again
    # Time: O(2 ^ N), 
    # Space: O(N) -> Recursion depth
    def fib_1(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        
        return self.fib(n - 1) + self.fib(n - 2)     # Two calls: 2 ^ n time
        