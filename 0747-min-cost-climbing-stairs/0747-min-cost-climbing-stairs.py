class Solution:

    # Space Optimization
    # Time: O(N), Space: O(1)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        prev2 = cost[0]
        prev1 = cost[1]

        for i in range(2, n):
            curi = cost[i] + min(prev1, prev2)
            prev2, prev1 = prev1, curi
        
        return min(prev1, prev2)



    # Tabulation (Bottom-Up DP)
    # Time: O(N), Space: O(N)
    def minCostClimbingStairs3(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * (n + 1)

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        
        return min(dp[n - 1], dp[n - 2])


    # Recursion + Memoization (Top-Down DP)
    # Time: O(N), Space: O(N) + O(N) (Stack + dp array)
    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * (n + 1)

        def _helper(ind):
            if ind >= len(cost):
                return 0
            
            if dp[ind] != -1:
                return dp[ind]

            jumpOne = cost[ind] + _helper(ind + 1)
            jumpTwo = cost[ind] + _helper(ind + 2)

            dp[ind] = min(jumpOne, jumpTwo)
            return dp[ind]

        return min(_helper(0), _helper(1))


    # Recursion => Time: O(2 ^ n), Space: O(N)
    def minCostClimbingStairs1(self, cost: List[int]) -> int:
        n = len(cost)
    
        def _helper(ind):
            if ind >= len(cost):
                return 0
            
            jumpOne = cost[ind] + _helper(ind + 1)
            jumpTwo = cost[ind] + _helper(ind + 2)

            return min(jumpOne, jumpTwo)

        return min(_helper(0), _helper(1))